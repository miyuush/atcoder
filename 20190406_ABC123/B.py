import math
dish = []
mini = 0
for i in range(5):
    d = input()
    dish.append(d)
for j in dish:
    if j[-1] != '0':
        mini = j
if mini == 0:
    mini = dish[0]
for k in dish:
    if (k[-1] <= mini[-1]) and k[-1] != '0':
        mini = k
for i in range(5):
    if dish[i] == mini:
        dish.pop(i)
        break
time = 0
for l in range(4):
    dish[l] = math.ceil((int(dish[l]) / 10)) * 10
    time += int(dish[l])
time += int(mini)
print(time)
