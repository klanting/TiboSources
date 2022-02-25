from Math import number_theorie as nt

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
for i in range(30):
    a = ((i*60)+1)/7
    print(a, i)