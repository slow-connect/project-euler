fib = [0, 1]
while fib[-1] < 4000000:
    fib.append(fib[-1] + fib[-2])
res = 0
for k in range(0, len(fib), 3):
    res += fib[k]
print(res)
