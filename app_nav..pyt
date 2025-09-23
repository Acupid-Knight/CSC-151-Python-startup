# app_nav.py
import asyncio
import json
from fastapi import FastAPI, Request, UploadFile, File
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from modules.mapping import OccupancyGrid
from modules.localization import Localizer
from modules.slam_stub import SLAMStub
from modules.rover_ai import RoverAI
from modules.obstacle_detector import detect_obstacles_from_scan

app = FastAPI(title="NASA SUITS Navigation & Rover AI")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Global demo objects (in-memory)
GRID = OccupancyGrid(width=120, height=120, resolution=0.5, origin=(-30.0, -30.0))
# seed some obstacles (boulders)
GRID.mark_circle(5.0, 3.0, 1.5)
GRID.mark_circle(-2.0, -4.0, 1.0)
GRID.mark_circle(10.0, -6.0, 2.0)

localizer = Localizer((0.0, 0.0, 0.0))
slam = SLAMStub()
rover_ai = RoverAI(GRID)
rover_ai.set_pose(0.0, 0.0, 0.0)

# simple in-memory sensor scan placeholder
LAST_SCAN = []

@app.get("/", response_class=HTMLResponse)
async def index():
    with open("static/index_nav.html", "r", encoding="utf-8") as f:
        return HTMLResponse(f.read())

@app.post("/api/scan")  # accept a mock scan (JSON list of points)
async def upload_scan(request: Request):
    data = await request.json()
    pts = data.get("points", [])
    global LAST_SCAN
    LAST_SCAN = pts
    # detect obstacles
    obstacles = detect_obstacles_from_scan(pts)
    # transform obstacles to world coords using current pose
    x,y,theta = localizer.get_pose()
    world_obs = []
    import math
    for o in obstacles:
        # rotate + translate
        rx = o["x"] * math.cos(theta) - o["y"] * math.sin(theta) + x
        ry = o["x"] * math.sin(theta) + o["y"] * math.cos(theta) + y
        world_obs.append({"x": rx, "y": ry, "r": o["r"]})
        # mark occupancy grid
        GRID.mark_circle(rx, ry, max(0.5, o["r"]))
    return {"detected": world_obs}

@app.post("/api/frame")
async def upload_frame(file: UploadFile = File(...)):
    data = await file.read()
    dx, dy, dtheta = slam.process_frame(data)
    # apply to localizer (simple IMU-like update)
    # compute linear velocity as hypot and angular from dtheta per fixed dt
    localizer.apply_imu(linear_vel=dx/0.1 if dx else 0.0, angular_vel=dtheta/0.1 if dtheta else 0.0, dt=0.1)
    return {"dx": dx, "dy": dy, "dtheta": dtheta, "pose": localizer.get_pose()}

@app.post("/api/set_goal")
async def set_goal(req: Request):
    data = await req.json()
    gx = float(data.get("x", 5.0))
    gy = float(data.get("y", 5.0))
    rover_ai.set_goal(gx, gy)
    return {"status": "goal_set", "goal": (gx, gy)}

@app.get("/api/get_map")
async def get_map():
    center = localizer.get_pose()
    slice_ = GRID.get_slice(center_x=center[0], center_y=center[1], span_m=40.0)
    return {"slice": slice_, "pose": localizer.get_pose(), "path": rover_ai.current_path, "state": rover_ai.state}

# SSE telemetry: pose, state, path, obstacles
async def telemetry_generator():
    while True:
        obs = []  # convert last scan to world obstacles
        import math
        x,y,theta = localizer.get_pose()
        # step rover AI using world obstacles
        # convert LAST_SCAN (points in rover frame) to obstacles
        obstacles = detect_obstacles_from_scan(LAST_SCAN)
        world_obs = []
        for o in obstacles:
            rx = o["x"] * math.cos(theta) - o["y"] * math.sin(theta) + x
            ry = o["x"] * math.sin(theta) + o["y"] * math.cos(theta) + y
            world_obs.append({"x": rx, "y": ry, "r": o["r"]})
        ai_state = rover_ai.step(obstacles_world=world_obs)
        # update localizer with controller pose to keep sync
        rp = rover_ai.controller.get_pose()
        localizer.pose = [rp[0], rp[1], rp[2]]
        payload = {"pose": localizer.get_pose(), "ai": ai_state, "path": rover_ai.current_path, "obstacles": world_obs, "grid_origin": GRID.origin}
        yield f"data: {json.dumps(payload)}\n\n"
        await asyncio.sleep(0.5)

@app.get("/api/telemetry")
async def telemetry():
    return StreamingResponse(telemetry_generator(), media_type="text/event-stream")
