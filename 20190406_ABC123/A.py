ant = []
for i in range(5):
    ant0 = int(input())
    ant.append(ant0)
k = int(input())
if ant[1] - ant[0] > k:
    print(':(')
elif ant[2] - ant[0] > k:
    print(':(')
elif ant[3] - ant[0] > k:
    print(':(')
elif ant[4] - ant[0] > k:
    print(':(')
else:
    print('Yay!')