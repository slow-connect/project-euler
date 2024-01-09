def sum_to_n(n):
    return n * (n + 1) // 2
def sum_of_squares(n):
    return n * (n + 1) * (2 * n + 1) // 6

def main():
    n = 100
    print(sum_to_n(n) ** 2 - sum_of_squares(n))
main()
