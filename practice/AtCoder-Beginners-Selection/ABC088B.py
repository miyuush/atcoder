N = int(input())
a = list(map(int, input().split()))
A = 0
B = 0
a.sort()
a.reverse()
for i in range(N):
    if (i % 2) == 0:
        A += a[i]
    else:
        B += a[i]
print(A-B)