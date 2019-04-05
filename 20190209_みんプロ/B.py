# 入力 a1-3, b1-3
a = []
b = []
for i in range(3):
    a0, b0 = [int(i) for i in input().split()]
    if a0 != b0:
        a.append(a0)
        b.append(b0)
    else:
        print("NO")

# 制約条件
if 1 <= all(a + b) <= 4:
    # 同じ街の間に複数の道がないように
    if a[0] + b[0] != a[1] + b[1] and a[1] + b[1] != a[2] + b[2] and a[2] + b[2] != a[0] + b[0]:
        one = (a + b).count(1)
        two = (a + b).count(2)
        three = (a + b).count(3)
        four = (a + b).count(4)
        if 1 <= one <=2 and 1 <= two <=2 and 1 <= three <=2 and 1 <= four <=2:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
else:
    print("NO")

