N = int(input())
s = [input() for i in range(N)]
cnt = 0
a = 0
b = 0
ab = 0
for i in range(N):
    cnt += s[i].count('AB')
for j in range(N):
    if s[j][0] == 'B' and s[j][-1] == 'A':
        ab += 1
    if s[j][-1] == 'A':
        a += 1
    if s[j][0] == 'B':
        b += 1
if a == b == ab and ab > 0:
    print(cnt+ab-1)
else:
    print(cnt+min(a, b))
