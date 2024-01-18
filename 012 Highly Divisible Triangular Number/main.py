from math import isqrt
def euler(n):
    return n*(n+1) // 2

def num_divisors(n):
    count = 0
    for i in range(1, isqrt(n)+1):
        if n % i == 0:
            if n // i == i:
                count += 1
            else:
                count += 2
    return count


def main():
    n=1
    while True:
        x = euler(n)
        if num_divisors(x) >= 500:
            return x
            break
        n += 1

print(main())
