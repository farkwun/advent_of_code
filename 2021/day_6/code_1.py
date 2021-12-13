f = open("input.txt", "r")
# f = open("sample.txt", "r")
fish = [int(num) for num in f.readline().split(",")]
f.close()

SIMULATION_WINDOW = 80

days = 0

while days < SIMULATION_WINDOW:
    new_fish = []
    for idx, f in enumerate(fish):
        if f == 0:
            fish[idx] = 6
            new_fish.append(8)
            continue
        fish[idx] -= 1
    fish.extend(new_fish)
    days += 1

print(len(fish))
