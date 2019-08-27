n, m = map(int, input().split())
foods = [0] * 31
for i in range(n):
    cnt = list(map(int, input().split()))
    for j in range(cnt[0]):
        foods[cnt[j + 1]] += 1

print(sum([1 for x in foods if x == n]))