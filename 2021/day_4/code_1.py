from collections import namedtuple

Point = namedtuple("Point", "row col")


class Board:
    ROWS = 5
    COLS = 5

    def __init__(self):
        self.board = [[False] * self.COLS for _ in range(self.ROWS)]
        self.board_vals = None
        self.indices = {}

    def populate_board(self, board_rows):
        self.board_vals = board_rows
        for row_idx, row in enumerate(board_rows):
            for col_idx, val in enumerate(row):
                self.indices[val] = Point(row_idx, col_idx)

    def set_and_check(self, val):
        if val not in self.indices:
            return False
        point = self.indices[val]
        self.board[point.row][point.col] = True
        return self.check_row(point.row) or self.check_col(point.col)

    def check_col(self, col):
        for row in self.board:
            if row[col] is False:
                return False
        return True

    def check_row(self, row):
        return all(self.board[row])

    def get_unmarked_sum(self):
        the_sum = 0
        for row_idx, row in enumerate(self.board):
            for col_idx, val in enumerate(row):
                if val is False:
                    the_sum += int(self.board_vals[row_idx][col_idx])
        return the_sum

    def print_board(self):
        for row in self.board:
            print(row)
        print("")


def row_to_nums(line):
    nums = line.split(" ")
    return [num for num in nums if num]


f = open("input.txt", "r")
# f = open("sample.txt", "r")
draws = f.readline().split(",")


boards = []
board_rows = []
temp_board = None

while True:
    line = f.readline()
    if not line:
        break

    if line == "\n":
        if temp_board is not None:
            temp_board.populate_board(board_rows)
            boards.append(temp_board)
        board_rows = []
        temp_board = None
        continue

    line = line.rstrip()

    if temp_board is None:
        temp_board = Board()

    row_nums = row_to_nums(line)
    board_rows.append(row_nums)

f.close()

for draw in draws:
    for board in boards:
        if board.set_and_check(draw):
            u_sum = board.get_unmarked_sum()
            print(draw, u_sum)
            print(int(draw) * u_sum)
            quit()
