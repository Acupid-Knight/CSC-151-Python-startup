import heapq, math

def heuristic(a, b):
    return math.hypot(a[0]-b[0], a[1]-b[1])

def cost(node, neighbor, costmap, slopemap, energy_weight=1.0, risk_weight=2.0):
    base = costmap.get_cost(neighbor)  # base terrain traversability
    slope = slopemap.get(neighbor, 0)
    risk = costmap.get_risk(neighbor)
    dist = math.hypot(neighbor[0]-node[0], neighbor[1]-node[1])
    # composite cost: distance + energy(slope) + risk penalty
    return dist + energy_weight * (1 + slope/10.0) + risk_weight * risk + base

def astar(start, goal, costmap, slopemap):
    openq = []
    heapq.heappush(openq, (heuristic(start, goal), 0, start, None))
    came_from = {}
    gscore = {start: 0}
    while openq:
        _, g, current, parent = heapq.heappop(openq)
        if current == goal:
            # reconstruct
            path = [current]
            while parent:
                path.append(parent)
                parent = came_from.get(parent)
            return list(reversed(path))
        came_from[current] = parent
        for nbr in costmap.neighbors(current):
            tentative = g + cost(current, nbr, costmap, slopemap)
            if tentative < gscore.get(nbr, float('inf')):
                gscore[nbr] = tentative
                f = tentative + heuristic(nbr, goal)
                heapq.heappush(openq, (f, tentative, nbr, current))
    return None  # no path

# On a dynamic update (new obstacles), re-run astar from current rover pose.





