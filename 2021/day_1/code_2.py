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

WIN_LEN = 3

window_sum = 0

w_st = w_end = 0

increases = 0

for m in measurements:
    if abs(w_st - w_end) < WIN_LEN:
        w_end += 1
        window_sum += m
        continue
    new_sum = window_sum - measurements[w_st] + m
    w_st += 1

    if new_sum > window_sum:
        increases += 1
    window_sum = new_sum
    w_end += 1

print(increases)


f.close()
