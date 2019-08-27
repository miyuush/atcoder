N = int(input())
d = list(map(int, input().split()))
d.sort()
n = int(N/2)

if d[n-1] - d[n] == 0:
    print(0)
else:
    print(abs(d[n-1] - d[n]))
