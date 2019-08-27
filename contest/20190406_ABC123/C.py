import math
n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
time = 0
a_b = int(n / a)
if n % a != 0:
    a_b += 1
time += a_b
if a <= b:
    b_c = a_b - 1
else:
    b_c = (math.ceil(a / b)) - 1
time += b_c
if b <= c:
    c_d = b_c
else:
    c_d = (math.ceil(b / c)) + 1
time += c_d
if c <= d:
    d_e = c_d
else:
    d_e = (math.ceil(c / d)) + 1
time += d_e
if d <= e:
    e_f = d_e
else:
    e_f = (math.ceil(d / e)) + 1
time += e_f
print(time)
