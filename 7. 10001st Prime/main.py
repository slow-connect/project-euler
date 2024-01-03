def sieve_of_eratosthenes():
    lst = [(i, True) for i in range(2, 150000)]
    cnt = 0
    num = -1
    for i in range(0, len(lst)):
        if lst[i][1]:
            for j in range(i + lst[i][0], len(lst), lst[i][0]):
                lst[j] = (lst[j][0], False)
            cnt += 1
            if cnt == 10001:
                num = lst[i][0]
    return num

def main():
    print(sieve_of_eratosthenes())



main()
