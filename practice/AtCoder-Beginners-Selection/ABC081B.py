N = int(input())
A = list(map(int, input().split()))
f = 0
r = 0
while(1):
    for i in range(N):
        if (A[i] % 2) != 0:
            f = 1
    if f:
        break
    for j in range(N):
        A[j] = A[j] / 2
    r += 1
print(r)
