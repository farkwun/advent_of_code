f = open("input.txt", "r")
diagnostics = []
for line in f:
    diagnostics.append(line.rstrip())
f.close()

# diagnostics = [
#    "00100",
#    "11110",
#    "10110",
#    "10111",
#    "10101",
#    "01111",
#    "00111",
#    "11100",
#    "10000",
#    "11001",
#    "00010",
#    "01010",
# ]

num_len = len(diagnostics[0])

gamma = []

i = 0
while i < num_len:
    one_count = 0
    for d in diagnostics:
        if d[i] == "1":
            one_count += 1
    gamma.append("1" if one_count > len(diagnostics) // 2 else "0")
    i += 1

epsilon = ["1" if val == "0" else "0" for val in gamma]

gamma = "".join(gamma)
epsilon = "".join(epsilon)

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

print(gamma * epsilon)
