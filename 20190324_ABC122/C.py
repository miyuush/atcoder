import sys

N, Q = map(int, sys.stdin.readline().split())
S = input()
s = []

for i in range(Q):
    l, r = map(int, sys.stdin.readline().split())
    s.append(S[l-1:r].count('AC'))

for j in range(Q):
    print(s[j])

