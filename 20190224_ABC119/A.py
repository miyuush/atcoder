import datetime
s = input()
S = datetime.datetime.strptime(s, '%Y/%m/%d')
base = datetime.datetime(2019, 4, 30)
if S == base or S <= base:
    print("Heisei")
else:
    print("TBD")