S = list(input())
d = {}
for i in range(len(S)):
    d[S[i]] = 1
if len(d) == 2:
    print('Yes')
else:
    print('No')
