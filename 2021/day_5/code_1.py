from collections import namedtuple

Point = namedtuple("Point", "row col")
Line = namedtuple("Line", "start end")

max_val = float("-inf")


def generate_point(point_string):
    global max_val
    col, row = point_string.rstrip().split(",")
    col, row = int(col), int(row)
    max_val = max(max_val, row, col)
    return Point(row, col)


def parse_line(line_string):
    start, end = line_string.rstrip().split("->")
    return Line(generate_point(start), generate_point(end))


def should_add(line):
    start, end = line
    return start.row == end.row or start.col == end.col


def draw_line(line, plane):
    # assume horizontal
    start, end = line
    if start.row == end.row:
        row = start.row
        col = min(start.col, end.col)
        max_col = max(start.col, end.col)
        while col <= max_col:
            plane[row][col] += 1
            col += 1
    else:
        col = start.col
        row = min(start.row, end.row)
        max_row = max(start.row, end.row)
        while row <= max_row:
            plane[row][col] += 1
            row += 1


def score(plane):
    score = 0
    for row_idx, row in enumerate(plane):
        for col_idx, val in enumerate(row):
            if val > 1:
                score += 1
    return score


f = open("input.txt", "r")
# f = open("sample.txt", "r")
lines = []
for line in f:
    parsed_line = parse_line(line)
    if should_add(parsed_line):
        lines.append(parse_line(line))

plane = [[0] * (max_val + 1) for _ in range(max_val + 1)]

for line in lines:
    draw_line(line, plane)

print(score(plane))

f.close()
