A, B = map(int, input().split())
ans = bin(B)
for i in range(A, B):
    ans = int(ans, 2) ^ int(bin(i), 2)
print(int(ans, 2))