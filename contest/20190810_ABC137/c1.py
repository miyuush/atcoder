import sys
def input():
    return sys.stdin.readline()[:-1]
d = {}
ans = 0
n = int(input())
s = [''.join(sorted(input())) for i in range(n)]
for string in s:
    if string in d:
        ans += d[string]
        d[string] += 1
    else:
        d[string] = 1
print(ans)
