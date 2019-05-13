N = int(input())
S = list(input())
p = 0
cnt_b = 0
cnt_w = 0
total = 0
while p < len(S):
    p += 1
    if S[p-1] == '#':
        cnt_b += 1
        if len(S) <= p:
            break
        elif S[p] == '.':
            while S[p] == '.':
                cnt_w += 1
                p += 1
                if len(S) <= p:
                    if cnt_b > cnt_w:
                        total += cnt_w
                    elif cnt_b < cnt_w:
                        total += cnt_b
                    else:
                        total += cnt_b
                    break
                elif S[p] == '#':
                    if cnt_b > cnt_w:
                        total += cnt_w
                    elif cnt_b < cnt_w:
                        total += cnt_b
                    else:
                        total += cnt_b
                    cnt_b = 0
                    cnt_w = 0
print(total)
