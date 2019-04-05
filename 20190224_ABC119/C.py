n, a, b, c = map(int, input().split())
l = [0] * (n+1)
mp = 0
absa = 0
absb = 0
absc = 0
for i in range(n):
    l[i] = int(input())

fl = len(l)
absa = abs(a-l[0])
absai = 0
absb = abs(b-l[0])
absbi = 0
absc = abs(c-l[0])
absci = 0
for i in range(n):
    if abs(a-l[i+1]) < absa:
        absa = abs(a-l[i+1])
        absai = i+1
    if abs(b-l[i+1]) < absb:
        absb = abs(b-l[i+1])
        absbi = i+1
    if abs(c-l[i+1]) < absc:
        absc = abs(c-l[i+1])
        absci = i+1

if absa == 0:
    l.remove(a)
    a = 0
elif absb == 0:
    l.remove(b)
    b = 0
elif absc == 0:
    l.remove(c)
    c = 0
if len(l)+3 == fl:
    print(mp)
for i in range(n):
    if a != 0 and any((x <= absa for x in l)):
        la = [y for y in l if y <= absa]
        absa -= max(la)
        mp += absa
    if b != 0 and any((x <= absb for x in l)):
        lb = [y for y in l if y <= absb]
        absb -= max(lb)
        mp += absb
    if c != 0 and any((x <= absc for x in l)):
        lc = [y for y in l if y <= absc]
        absc -= max(lc)
        mp += absc
print(mp)



