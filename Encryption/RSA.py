import random
from Math import number_theorie as nt
import matplotlib.pyplot as pyplot
import time
def run():
    p = 5
    q = 11
    n = p * q
    relative_primes = (p-1)*(q-1)

    e = 7
    d = 23

    a = nt.convert(e*d, relative_primes)


    encrypted = nt.convert(5**e, n)

    decrypted = nt.convert(encrypted**d, n)

    print(encrypted)
    print(decrypted)

def train(e, phi):
    for i in range(1, phi):
        a = ((i*phi+1)/e)
        print(i, a)



def test(a, max, mod):
    for i in range(max):

        print(a*i, (a*i)%mod)


def find_d(e, phi):
    for i in range(1, phi):
        a = ((i*phi+1)/e)
        if a % 1 == 0:
            return a

def find_d_2(e, phi):
    lst = []
    div = phi
    divr = e
    while True:
        a = int(div/divr)
        #print("diver", div, divr)
        a_rest = div % divr
        lst.append([div, a, divr, a_rest])
        #print(a_rest)
        if a_rest == 1:
            break
        div = divr
        divr = a_rest

    print(lst)

    value = 1
    for l in lst:
        value *= l[1]
    print(value)
    value += lst[0][1]
    value += 1
    print(phi, value)
    return phi-value

#print(find_d(5, 132))
#print(find_d_2(5, 132))
#print(find_d(3581, 4621))
#print(find_d_2(3581, 4621))
#print(3581*2937.0)



def mi(a, b):
    """Returns a tuple (r, i, j) such that r = gcd(a, b) = ia + jb
    """

    x = 0
    y = 1
    lx = 1
    ly = 0
    oa = a
    ob = b

    while b != 0:
        q = a // b
        (a, b) = (b, a % b)
        (x, lx) = ((lx - (q * x)), x)
        (y, ly) = ((ly - (q * y)), y)
    if lx < 0:
        lx += ob
    if ly < 0:
        ly += oa

    return lx

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
print(10**(40*14) % 55)
p = 11
q = 5
n = p*q
phi = (p-1)*(q-1)
e = 17
d = mi(e, phi)
a = 10
a = (a**e)
a = (a**d) % n
print(a)
print((a**phi) % n)
k = (e*d-1)/phi
print("k", k)
print(e*d)
print(10**(int(k*phi)) % n)
"""
lst = []
t_1 = 0
for i in range(5, 100005):
    #print(1, i)
    e = i-1
    while True:
        if gcd(e, i) == 1:
            break

    ts = time.perf_counter()
    d = mi(e, i)
    te = time.perf_counter()
    lst.append(te-ts)
    t_1 += te-ts
"""
"""
lst_2 = []
t_2 = 0
for i in range(5, 100000):
    print(2, i)
    e = i-1
    while True:
        if gcd(e, i) == 1:
            break

    ts = time.perf_counter()
    d = find_d(e, i)
    te = time.perf_counter()
    lst_2.append(te-ts)
    t_2 += te - ts

print(t_1, t_2 )
"""
#pyplot.plot(lst_2, color="b")
#pyplot.plot(lst, color="y")
#pyplot.show()

#print(mi(3581, 4621))

