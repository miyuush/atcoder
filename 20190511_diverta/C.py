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
    elif s[j][-1] == 'A':
        a += 1
    elif s[j][0] == 'B':
        b += 1
if ab > 1:
    ab -= 1
    if ab % 2 == 0:
        print(cnt+min(a, b)+ab)
    else:
        print(cnt+max(a, b)+ab)
else:
    print(cnt+min(a, b))
