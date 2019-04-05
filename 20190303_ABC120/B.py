a, b, k = map(int, input().split())
num = []
mini = min(a, b)
for i in range(1, mini+1):
    if a % i == 0 and b % i == 0:
        num.append(i)
num.sort()
num.reverse()
print(num[k-1])