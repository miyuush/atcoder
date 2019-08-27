N, M, C = map(int, input().split())
B = list(map(int, input().split()))
ans = 0
s = 0

for _ in range(N):
    A = list(map(int, input().split()))
    for i in range(M):
        s += A[i] * B[i]
    s += C
    if s > 0:
        ans += 1
    s = 0
print(ans)

