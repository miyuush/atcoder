N, X = map(int, input().split())
S = list(map(int, input().split()))
ans = 0


def gcd(x, y):
    while y != 0:
        x, y = y, x % y
        if int(x / y) == 1:
            return x % y
        if y == 1:
            return y
    return y


print(gcd(82, 22))

# if any([i == 1 for i in S]):
#     print(0)
for i in range(N):
    ans += gcd(X, S[i])
print(ans)




