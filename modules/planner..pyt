# modules/planner.py
"""
A* grid planner on occupancy grid. Returns path as list of world coords.
"""

import heapq
import math
from typing import List, Tuple, Optional

def heuristic(a: Tuple[int,int], b: Tuple[int,int]) -> float:
    return math.hypot(a[0]-b[0], a[1]-b[1])

def astar(grid, start_cell: Tuple[int,int], goal_cell: Tuple[int,int]) -> Optional[List[Tuple[int,int]]]:
    h = heuristic
    neighbors = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
    w = len(grid[0])
    hgt = len(grid)
    closed = set()
    came_from = {}
    gscore = {start_cell: 0}
    fscore = {start_cell: h(start_cell, goal_cell)}
    open_heap = [(fscore[start_cell], start_cell)]
    while open_heap:
        _, current = heapq.heappop(open_heap)
        if current == goal_cell:
            # reconstruct path
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path
        closed.add(current)
        for dx, dy in neighbors:
            nb = (current[0]+dx, current[1]+dy)
            if not (0 <= nb[0] < hgt and 0 <= nb[1] < w):
                continue
            if grid[nb[0]][nb[1]] == 1:
                continue  # occupied
            tentative_g = gscore[current] + math.hypot(dx, dy)
            if nb in closed and tentative_g >= gscore.get(nb, float('inf')):
                continue
            if tentative_g < gscore.get(nb, float('inf')) or nb not in [i[1] for i in open_heap]:
                came_from[nb] = current
                gscore[nb] = tentative_g
                fscore[nb] = tentative_g + h(nb, goal_cell)
                heapq.heappush(open_heap, (fscore[nb], nb))
    return None
