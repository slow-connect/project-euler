def main():
    for a in range(1, 333):
        k = (1000 - a)
        for b in range(a+1, k):
            c = k - b
            if a**2 + b**2 == c**2:
                print(a*b*c)
                return


main()
