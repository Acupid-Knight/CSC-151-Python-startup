# modules/mapping.py
"""
Occupancy grid mapping and terrain visualization utilities.
Grid coordinates: (i, j) => world coords using resolution.
"""

import numpy as np
from typing import Tuple, List, Dict

class OccupancyGrid:
    def __init__(self, width=100, height=100, resolution=0.5, origin=(-25.0, -25.0)):
        # width/height in cells
        self.width = width
        self.height = height
        self.resolution = resolution
        self.origin = origin  # world coords of grid (0,0) cell
        # -1 unknown, 0 free, 1 occupied
        self.grid = np.full((height, width), -1, dtype=int)

    def world_to_cell(self, x: float, y: float) -> Tuple[int, int]:
        ox, oy = self.origin
        i = int((y - oy) / self.resolution)
        j = int((x - ox) / self.resolution)
        i = max(0, min(self.height - 1, i))
        j = max(0, min(self.width - 1, j))
        return i, j

    def set_occupied(self, x: float, y: float):
        i, j = self.world_to_cell(x, y)
        self.grid[i, j] = 1

    def set_free(self, x: float, y: float):
        i, j = self.world_to_cell(x, y)
        self.grid[i, j] = 0

    def mark_circle(self, x: float, y: float, radius: float):
        # mark cells within radius as occupied
        cx, cy = x, y
        r_cells = int(radius / self.resolution)
        ci, cj = self.world_to_cell(cx, cy)
        for di in range(-r_cells, r_cells + 1):
            for dj in range(-r_cells, r_cells + 1):
                ii = ci + di
                jj = cj + dj
                if 0 <= ii < self.height and 0 <= jj < self.width:
                    self.grid[ii, jj] = 1

    def get_slice(self, center_x: float, center_y: float, span_m: float = 30.0) -> Dict:
        # returns a small viewport for visualization
        half = int((span_m / 2) / self.resolution)
        ci, cj = self.world_to_cell(center_x, center_y)
        i0 = max(0, ci - half)
        i1 = min(self.height, ci + half)
        j0 = max(0, cj - half)
        j1 = min(self.width, cj + half)
        sub = self.grid[i0:i1, j0:j1].tolist()
        return {"grid": sub, "origin_cell": (i0, j0), "center_cell": (ci, cj), "resolution": self.resolution}
