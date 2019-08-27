N, Y = map(int, input().split())
x, y, z = 0, 0, 0
for i in range(N+1):
    for j in range(N+1):
        k = N - i - j
        if (10000 * i) + (5000 * j) + (1000 * k) == Y and k >= 0:
            x = i
            y = j
            z = k
if x == y == z == 0:
    print(-1, -1, -1)
else:
    print(x, y, z)