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
    return True
    # horizontal/vertical check logic - unnecessary for part 2
    # start, end = line
    # return start.row == end.row or start.col == end.col


def print_plane(plane):
    for row in plane:
        print(row)


def h_draw(line, plane):
    start, end = line
    row = start.row
    col = min(start.col, end.col)
    max_col = max(start.col, end.col)
    while col <= max_col:
        plane[row][col] += 1
        col += 1


def v_draw(line, plane):
    start, end = line
    col = start.col
    row = min(start.row, end.row)
    max_row = max(start.row, end.row)
    while row <= max_row:
        plane[row][col] += 1
        row += 1


def diag_draw(line, plane):
    start, end = line
    s_row, s_col = start.row, start.col
    e_row, e_col = end.row, end.col

    direction = (
        ((e_row - s_row) // abs(e_row - s_row)),
        ((e_col - s_col) // abs(e_col - s_col)),
    )

    conditionals = {
        (1, 1): lambda s_row, e_row, s_col, e_col: s_row <= e_row and s_col <= e_col,
        (-1, -1): lambda s_row, e_row, s_col, e_col: s_row >= e_row and s_col >= e_col,
        (-1, 1): lambda s_row, e_row, s_col, e_col: s_row >= e_row and s_col <= e_col,
        (1, -1): lambda s_row, e_row, s_col, e_col: s_row <= e_row and s_col >= e_col,
    }

    cond = conditionals[direction]
    while cond(s_row, e_row, s_col, e_col):
        plane[s_row][s_col] += 1
        s_row += direction[0]
        s_col += direction[1]


def draw_line(line, plane):
    start, end = line

    if start.row == end.row:
        h_draw(line, plane)
    elif start.col == end.col:
        v_draw(line, plane)
    else:
        diag_draw(line, plane)


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
