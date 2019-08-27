N = int(input())
t = []
x = []
y = []
for _ in range(N):
    t0, x0, y0 = map(int, input().split())
    t.append(t0)
    x.append(x0)
    y.append(y0)
for i in range(N):
    flag = False
    if t[i] >= x[i] + y[i]:
        if (t[i] % 2) == ((x[i]+y[i]) % 2):
            flag = True
        else:
            break
    else:
        break
if flag:
    print('Yes')
else:
    print('No')
