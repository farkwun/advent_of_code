f = open("input.txt", "r")
# f = open("sample.txt", "r")
inputs = [int(num) for num in f.readline().split(",")]
f.close()

SIM_DAYS = 256

DEFAULT_SPAWN_DAYS = 7

DEFAULT_SPAWN_BUFFER = 2

fishes = {spawn_days: 0 for spawn_days in range(10)}

for f in inputs:
    fishes[f] += 1


for day in range(1, SIM_DAYS + 1):
    fishes[DEFAULT_SPAWN_DAYS] += fishes[0]
    fishes[DEFAULT_SPAWN_DAYS + DEFAULT_SPAWN_BUFFER] += fishes[0]

    new_fishes = {spawn_days: 0 for spawn_days in range(10)}
    new_fishes.update({f - 1: fishes[f] for f in fishes.keys() if f > 0})

    num_fishes = sum(new_fishes.values())

    fishes = new_fishes

    print(day, num_fishes)
