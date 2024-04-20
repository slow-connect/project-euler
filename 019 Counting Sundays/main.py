
def main():
    days = 0
    res = 0
    for k in range(1900, 2001):
        for i in range(1, 13):
            if days % 7 == 6 and k > 1900 and k < 2001:
                res += 1
            if i == 4 or i == 6 or i == 9 or i == 11:
                days += 30
            elif i == 2:
                if k % 400:
                    days += 29
                elif k % 100:
                    days += 28
                elif k % 4:
                    days += 29
                else:
                    days += 28
            else:
                days += 31
    print(res)

if __name__ == '__main__':
    main()
