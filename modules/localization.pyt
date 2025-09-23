# modules/localization.py
"""
Localization stubs: simple sensor fusion combining IMU delta pose and beacon fixes.
Replace IMU/beacon with real telemetry in production.
"""

from typing import Dict, Tuple, Optional
import math
import time

class Localizer:
    def __init__(self, init_pose=(0.0, 0.0, 0.0)):
        # pose: (x, y, theta) in meters, radians
        self.pose = list(init_pose)
        self.last_update = time.time()

    def apply_imu(self, linear_vel: float, angular_vel: float, dt: float):
        # simple constant-velocity motion model update
        x, y, theta = self.pose
        dx = linear_vel * math.cos(theta) * dt
        dy = linear_vel * math.sin(theta) * dt
        dtheta = angular_vel * dt
        self.pose[0] += dx
        self.pose[1] += dy
        self.pose[2] += dtheta
        return tuple(self.pose)

    def apply_beacon_fix(self, beacon_pos: Tuple[float, float], measured_range: float):
        # very simple triangulation-like correction: move towards estimated location
        bx, by = beacon_pos
        # crude correction: place rover on circle around beacon along current heading
        theta = self.pose[2]
        est_x = bx - measured_range * math.cos(theta)
        est_y = by - measured_range * math.sin(theta)
        # blend / fuse (alpha)
        alpha = 0.6
        self.pose[0] = alpha * est_x + (1 - alpha) * self.pose[0]
        self.pose[1] = alpha * est_y + (1 - alpha) * self.pose[1]
        return tuple(self.pose)

    def get_pose(self) -> Tuple[float, float, float]:
        return tuple(self.pose)