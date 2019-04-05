N, M = map(int, input().split())
AB = [list(map(int, input().split())) for i in range(N)]
cnt = 0
yen = 0

sortkey = lambda val: val[0]
AB.sort(key=sortkey)

for i in range(N):
    if M >= AB[i][1]:
        cnt += AB[i][1]
        yen += AB[i][0] * AB[i][1]
        M -= AB[i][1]
    elif M < AB[i][1]:
        cnt += M
        yen += AB[i][0] * M
        M = 0
    if M == 0:
        print(yen)
        break