n = 1000000

def collatz(n, look_up):
    if n == 1:
        return 1
    elif n % 2 == 0:
        if n // 2 >= len(look_up):
            return 1 + collatz(n // 2, look_up)
        elif look_up[n // 2] != 0:
            return 1 + look_up[n // 2]
        else:
            return 1 + collatz(n // 2, look_up)
    else:
        if 3*n + 1 >= len(look_up):
            return 1 + collatz(3*n + 1, look_up)
        elif look_up[3*n + 1] != 0:
            return 1 + look_up[3*n + 1]
        else:
            return 1 + collatz(3*n + 1, look_up)



look_up = [0 for _ in range(n)]
look_up[1] = 1
length = [0 for _ in range(n)]

max = 0
max_num = 0
for i in range(1, n):
    x = collatz(i, look_up)
    length[i] = x
    if x > max:
        max = x
        max_num = i
print(max_num)


# Set `True` to plot
if False:
    import matplotlib.pyplot as plt
    plt.plot(length, '.')
    plt.show()
