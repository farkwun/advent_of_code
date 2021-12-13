f = open("input.txt", "r")
# f = open("sample.txt", "r")
crabs = [int(num) for num in f.readline().split(",")]
f.close()


positions = [0] * (max(crabs) + 1)


def get_fuel_cost(st, ed):
    # use gauss summation
    n = abs(st - ed)
    return (n * (n + 1)) // 2


for idx, _ in enumerate(positions):
    for c in crabs:
        positions[idx] += get_fuel_cost(c, idx)

min_idx = None
min_val = float("inf")

for idx, p in enumerate(positions):
    if p < min_val:
        min_val = p
        min_idx = idx

print(min_idx, positions[min_idx])
