N, A, B = map(int, input().split())
temp = 0
total = 0
for i in range(1, N+1):
    cnt = 0
    temp = i
    cnt += temp % 10
    while int(temp / 10) != 0:
        temp = int(temp/10)
        cnt += int(temp % 10)
    if A <= cnt <= B:
        total += i
print(total)