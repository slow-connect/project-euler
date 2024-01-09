def main():
    n = 2000000
    lst = [True for i in range(n)]
    ans = 0
    for i in range(2, len(lst)):
        if lst[i]:
            for j in range(2*i, len(lst), i):
                lst[j] = False
            ans += i

    print(ans)

main()
