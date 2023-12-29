from math import log
primes = [True for i in range(20)]
primes[0], primes[1] = False, False
for j in range(2, 20):
    for k in range(2*j, 20, j):
        primes[k] = False
pow = [0 for i in range(20)]
for k in range(20):
    if primes[k]:
        if log(20) / log(k) > 1:
            pow[k] = int(log(20) / log(k))
ans = 1
for k in range(20):
    if primes[k]:
        ans *= k ** pow[k]
print(ans)
