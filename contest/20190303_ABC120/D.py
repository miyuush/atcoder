# Union-findを使う
# 論文検索には(Disjoint Set)


from scipy.special import comb

n, m = map(int, input().split())
a = []
b = []
for i in range(m):
    a0, b0 = [int(i) for i in input().split()]
    a.append(a0)
    b.append(b0)

a.append(b)
l = len(a)
cmb = comb(m, 2, exact=True)
base = int(cmb / 2) + 1

for _ in range(m):
    l -= 2
    if l > base:
        print(0)
    elif l == 4:
        print(cmb-2)
    elif l == 2:
        print(cmb-1)
    elif l == 0:
        print(cmb)
    else:
        print(base)
        base += 1