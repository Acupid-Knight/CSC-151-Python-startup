# modules/slam_stub.py
"""
SLAM stub: accepts frames (simulated) and returns incremental pose deltas.
In production: integrate visual odometry / LiDAR SLAM (ORB-SLAM, Cartographer, RTAB-Map).
"""

import numpy as np
from typing import Tuple

class SLAMStub:
    def __init__(self):
        self.step = 0

    def process_frame(self, frame_bytes: bytes) -> Tuple[float, float, float]:
        """
        Mock: generate a small forward motion and small heading drift.
        """
        rng = np.random.RandomState(len(frame_bytes) % 97 + self.step)
        dx = float(0.05 + rng.normal(0, 0.01))  # forward meters
        dy = float(rng.normal(0, 0.005))
        dtheta = float(rng.normal(0, 0.005))
        self.step += 1
        return dx, dy, dtheta
