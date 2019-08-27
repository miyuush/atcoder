# 入力 K A B
kab = list(map(int, input().split()))

count = 0
bis = 1
yen = 0

# 制約条件
if 1 <= kab[0] <= 10**9 and 1 <= kab[1] <= 10**9 and 1 <= kab[2] <= 10**9:
    while count < kab[0]:
        if kab[1] < kab[2]:
            if yen > 0:
                bis += kab[2]
                yen = yen - 1
                count += 1
            elif bis < kab[1]:
                bis += 1
                count += 1
            else:
                 bis = bis - kab[1]
                 yen = 1
                 count += 1

        else:
            bis += 1
            count += 1
    print(bis)