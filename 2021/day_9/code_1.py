from collections import namedtuple

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


risk = 0
for row_idx, row in enumerate(grid):
    for col_idx, val in enumerate(row):
        if is_point_low(Point(row_idx, col_idx)):
            risk += grid[row_idx][col_idx] + 1

print(risk)
