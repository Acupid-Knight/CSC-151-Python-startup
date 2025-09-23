# modules/rover_control.py
"""
Simple rover control emulator: accepts velocity commands and updates simulated pose.
In production this would interface with motor controllers and safety systems.
"""

import time
import math

class RoverController:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0
        self.last_ts = time.time()

    def set_pose(self, x, y, theta):
        self.x, self.y, self.theta = x, y, theta

    def step_velocity(self, linear, angular, dt=None):
        if dt is None:
            now = time.time()
            dt = now - self.last_ts
            self.last_ts = now
        # update simple differential-drive kinematics
        self.x += linear * math.cos(self.theta) * dt
        self.y += linear * math.sin(self.theta) * dt
        self.theta += angular * dt
        return (self.x, self.y, self.theta)

    def get_pose(self):
        return (self.x, self.y, self.theta)
