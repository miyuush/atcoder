a, b, c = map(int, input().split())

if int(b / a) >= c:
    print(c)
else:
    print(int(b/a))