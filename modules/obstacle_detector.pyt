# modules/obstacle_detector.py
"""
Obstacle detector stub: from "sensor" data produce obstacle list.
Replace with CV/LiDAR pipeline in production.
"""

from typing import List, Tuple
import numpy as np

def detect_obstacles_from_scan(scan_points: List[Tuple[float, float]]) -> List[Dict]:
    """
    Accept 2D range points (x,y) in rover frame and return obstacles.
    For demo: cluster and return bounding circles.
    """
    if not scan_points:
        return []
    pts = np.array(scan_points)
    # trivial clustering: group by distance threshold
    clusters = []
    used = set()
    for i, p in enumerate(pts):
        if i in used:
            continue
        cluster = [p]
        used.add(i)
        for j in range(i+1, len(pts)):
            if j in used: continue
            if np.linalg.norm(p - pts[j]) < 0.5:
                cluster.append(pts[j])
                used.add(j)
        clusters.append(np.array(cluster))
    out = []
    for c in clusters:
        center = c.mean(axis=0)
        radius = np.max(np.linalg.norm(c - center, axis=1))
        out.append({"x": float(center[0]), "y": float(center[1]), "r": float(radius)})
    return out
