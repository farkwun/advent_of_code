f = open("input.txt", "r")
measurements = []
for line in f:
    measurements.append(int(line))

# measurements = [
#    199,
#    200,
#    208,
#    210,
#    200,
#    207,
#    240,
#    269,
#    260,
#    263,
# ]

last = float("inf")
increases = 0

for m in measurements:
    if m > last:
        increases += 1
    last = m

print(increases)


f.close()
