n = int(input())
hp = [0] * n
hp = list(map(int, input().split()))

hp = list(set(hp))
if len(hp) == 1:
    print(hp[0])
elif min(hp) == 1:
    print(1)
elif any((x % 2 == 1 for x in hp)):
    print(1)
elif min(hp) == 2:
    print(2)
elif min(hp) > 2:
    diff = [0] * n
    for i in range(len(hp)-1):
        diff[i] = abs(hp[i] - hp[i+1])
    print(min(y > 0 for y in diff))