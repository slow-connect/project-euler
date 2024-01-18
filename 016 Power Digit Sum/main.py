from math import pow

def main():
    n = 1000
    strg = str(int(pow(2, n)))
    sum = 0
    for k in strg:
        sum += int(k)
    return sum

val = main()
print(val)
