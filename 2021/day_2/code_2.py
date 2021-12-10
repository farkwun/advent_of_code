f = open("input.txt", "r")
commands = []
for line in f:
    commands.append(line)
f.close()

# commands = [
#    "forward 5",
#    "down 5",
#    "forward 8",
#    "up 3",
#    "down 8",
#    "forward 2",
# ]

h = d = aim = 0


def go_up(val):
    global aim
    aim -= val


def go_down(val):
    global aim
    aim += val


def go_forward(val):
    global h, d
    h += val
    d += aim * val


COMMAND_DICT = {
    "forward": lambda val: go_forward(val),
    "down": lambda val: go_down(val),
    "up": lambda val: go_up(val),
}


def parse_command(command):
    c, val = command.split(" ")
    return c, int(val)


for c in commands:
    com, val = parse_command(c)
    COMMAND_DICT[com](val)


print(h * d)
