S = input()
s = S[::-1]
a = ['dream', 'dreamer', 'erase', 'eraser']
for i in range(4):
    a[i] = a[i][::-1]
i = 0
while i < len(s):
    cond = False
    for j in range(4):
        if s[i:i+len(a[j])] == a[j]:
            i += len(a[j])
            cond = True
    if not cond:
        break
if cond:
    print('YES')
else:
    print('NO')
