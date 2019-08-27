# 入力 N K
nk = list(map(int, input().split()))

# 制約条件
if nk[0] > 0 and 0 <= nk[1] < 101:
    if nk[0] >= nk[1]:
        s = int(nk[0] / 2)
        j = nk[0] % 2
        if nk[1] <= s + j:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
else:
    print("NO")
