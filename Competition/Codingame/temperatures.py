import math
a = math.inf
n = int(input())
if n == 0:
    a = 0
else:
    for i in input().split():
        t = int(i)
        if abs(t) < abs(a):
            a = t
        elif abs(t) == abs(a):
            if t > 0:
                a = t
print(a)