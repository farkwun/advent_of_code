from collections import namedtuple
import heapq

Point = namedtuple("Point", "row col")

f = open("input.txt", "r")
# f = open("sample.txt", "r")
grid = []
for line in f:
    grid.append([int(height) for height in list(line.rstrip())])
f.close()

DIRS = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def get_from_grid(point):
    row, col = point
    if row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]):
        return grid[row][col]
    return float("inf")


def is_point_low(point):
    row, col = point
    val = grid[row][col]
    is_low = True
    for d in DIRS:
        new_point = Point(row + d[0], col + d[1])
        if val >= get_from_grid(new_point):
            is_low = False
            break
    return is_low


def should_basin_traverse(point, visited):
    row, col = point
    return (
        row >= 0
        and row < len(grid)
        and col >= 0
        and col < len(grid[0])
        and point not in visited
        and grid[row][col] != 9
    )


low_points = set()
for row_idx, row in enumerate(grid):
    for col_idx, val in enumerate(row):
        new_point = Point(row_idx, col_idx)
        if is_point_low(new_point):
            low_points.add(new_point)


visited = set()
basins = {}
for p in low_points:
    q = [p]
    area = 0
    while q:
        length = len(q)
        for i in range(length):
            point = q[i]
            visited.add(point)
            area += 1
            for d in DIRS:
                new_point = Point(point.row + d[0], point.col + d[1])
                if should_basin_traverse(new_point, visited):
                    q.append(new_point)
                    visited.add(new_point)
        q = q[length:]
    basins[p] = area


K = 3
top_k = []
for area in basins.values():
    if len(top_k) < K:
        heapq.heappush(top_k, area)
        continue
    if area > top_k[0]:
        heapq.heapreplace(top_k, area)


product = 1
for area in top_k:
    product *= area

print(product)
