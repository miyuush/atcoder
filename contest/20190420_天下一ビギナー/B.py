N = int(input())
S = list(input())
K = int(input())
p = S[K-1]
for i in range(N):
    if S[i] != p:
        S[i] = '*'
print("".join(S))
