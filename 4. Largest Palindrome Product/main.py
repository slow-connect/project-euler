max = 0

def is_palindrome(n):
    strg = str(n)
    for i in range(0, len(strg)):
        if strg[i] != strg[len(strg)-i-1]:
            return False
    return True

for k in range(0, 1000):
    for j in range(0, 1000):
        if is_palindrome(k*j) and k*j > max:
            max = k*j

print(max)
