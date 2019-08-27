r, g, b, n = map(int, input().split())
conb = 0
for i in range(n+1):
    for j in range(n+1):
        k = (n-(i*r)-(j*g))
        if ((i*r) + (j*g) + k) == n and k % b == 0 and k >= 0:
            conb += 1
print(conb)