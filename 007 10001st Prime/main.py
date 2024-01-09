def sieve_of_eratosthenes():
    lst = [True for i in range(150000)]
    cnt = 0
    num = -1
    for i in range(2, len(lst)):
        if lst[i]:
            for j in range(2*i, len(lst), i):
                lst[j] = False
            cnt += 1
            if cnt == 10001:
                num = i
    return num

def main():
    print(sieve_of_eratosthenes())



main()
