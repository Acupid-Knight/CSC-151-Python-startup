# modules/rover_ai.py
"""
Mission manager + autonomy stack:
- receives goals (world coords)
- queries occupancy grid and planner
- executes path step-by-step via rover controller
- handles obstacle detection + replanning
"""

from typing import Tuple, List, Optional, Dict
import time, math

from modules.mapping import OccupancyGrid
from modules.planner import astar
from modules.rover_control import RoverController

class RoverAI:
    def __init__(self, grid: OccupancyGrid):
        self.grid = grid
        self.controller = RoverController()
        self.current_path = []
        self.goal = None
        self.state = "idle"
        self.step_index = 0
        self.last_exec_t = time.time()

    def set_pose(self, x, y, theta):
        self.controller.set_pose(x, y, theta)

    def set_goal(self, x, y):
        self.goal = (x, y)
        self.plan_path()

    def plan_path(self):
        # compute start/goal in grid cells
        sx, sy, _ = self.controller.get_pose()
        si, sj = self.grid.world_to_cell(sx, sy)
        gi, gj = self.grid.world_to_cell(self.goal[0], self.goal[1])
        path_cells = astar(self.grid.grid.tolist(), (si, sj), (gi, gj))
        if path_cells is None:
            self.current_path = []
            self.state = "no_path"
        else:
            # convert path cells back to world coordinates (center of cell)
            res = self.grid.resolution
            ox, oy = self.grid.origin
            world_path = []
            for (ci, cj) in path_cells:
                wy = oy + (ci + 0.5) * res
                wx = ox + (cj + 0.5) * res
                world_path.append((wx, wy))
            self.current_path = world_path
            self.state = "planned"
            self.step_index = 0

    def step(self, obstacles_world: Optional[List[Dict]] = None) -> Dict:
        # Called in loop by app: executes next micro-step
        now = time.time()
        dt = now - self.last_exec_t
        if dt <= 0:
            dt = 0.1
        self.last_exec_t = now

        if self.state == "idle":
            return {"state": self.state}

        if self.state == "no_path":
            return {"state": self.state, "message": "cannot reach goal"}

        if self.state == "planned":
            # execute simple go-to next path point
            if self.step_index >= len(self.current_path):
                self.state = "arrived"
                return {"state": self.state}
            target = self.current_path[self.step_index]
            x,y,theta = self.controller.get_pose()
            dx = target[0] - x
            dy = target[1] - y
            dist = math.hypot(dx, dy)
            desired_theta = math.atan2(dy, dx)
            # heading error
            heading_err = (desired_theta - theta + math.pi) % (2*math.pi) - math.pi
            # control law: rotate then forward
            if abs(heading_err) > 0.2:
                linear = 0.0
                angular = 0.8 * heading_err
            else:
                linear = min(0.4, dist)  # m/s
                angular = 0.1 * heading_err
            # simple obstacle check: if an obstacle too close in front, stop and replan
            stop_due_obstacle = False
            if obstacles_world:
                for o in obstacles_world:
                    ox = o["x"]
                    oy = o["y"]
                    orad = o["r"] + 0.5
                    if math.hypot(ox - x, oy - y) < orad + 0.5:
                        stop_due_obstacle = True
                        break
            if stop_due_obstacle:
                self.state = "replanning"
                self.plan_path()
                return {"state": "replanning"}
            # apply to controller
            new_pose = self.controller.step_velocity(linear, angular, dt)
            # if close enough, advance to next waypoint
            if dist < 0.3:
                self.step_index += 1
            return {"state": self.state, "pose": new_pose, "target": target, "step_index": self.step_index}
        return {"state": self.state}
