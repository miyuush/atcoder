
N, K = map(int, input().split())
ans = 0

for i in range(1, K+1):
    if i == 1:
        t = i+(N-K)
        ans = t
    else:
        ans = t**(i-1)*(N-K)
    print(ans % (10**9 + 7))
