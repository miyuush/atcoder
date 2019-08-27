k, x = map(int, input().split())
p = []
for point in range(x-k+1, x+k):
    p.append(point)
print(' '.join(map(str, p)))