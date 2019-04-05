S = list(input())
l = [0] * 5
ind = 0
f = True

for i in range(len(S)):
    if (S[i] == 'A' or S[i] == 'C' or S[i] == 'G' or S[i] == 'T') and f:
        l[ind] += 1
    elif (S[i] == 'A' or S[i] == 'C' or S[i] == 'G' or S[i] == 'T') and f == False:
        l[ind] += 1
    else:
        f = False
        ind += 1
print(max(l))