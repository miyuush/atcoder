import sys
def input():
    return sys.stdin.readline()[:-1]

n = int(input())
s = [input() for i in range(n)]
cnt = 0
for i in range(0, n-1):
    stype1 = {}
    for j in range(10):
        if s[i][j] in stype1:
            stype1[s[i][j]] += 1
        else:
            stype1[s[i][j]] = 1
    for k in range(i+1, n):
        stype2 = {}
        for l in range(10):
            if s[k][l] in stype2:
                stype2[s[k][l]] += 1
            else:
                stype2[s[k][l]] = 1
        if stype1 == stype2:
            cnt += 1
print(cnt)