from math import isqrt as sqrt
n = 600851475143
primes = []

def is_prime(n):
    if n<= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = sqrt(n)
    for i in range(5, limit + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

for k in range(1, sqrt(n)+ 1):
    if n % k == 0:
        if is_prime(k):
            primes.append(k)
print(max(primes))
