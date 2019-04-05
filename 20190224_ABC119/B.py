n = int(input())
jpy = 0
btc = 0.0
for _ in range(n):
    money = list(input().split())
    if money[1] == 'JPY':
        jpy += int(money[0])
    else:
        btc += float(money[0])

print(jpy + (btc/1.0)*380000.0)