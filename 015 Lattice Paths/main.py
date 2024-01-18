from math import factorial
def main():
    N = 40
    K = 20
    return factorial(N) // factorial(K) // factorial(K)

print(main())
