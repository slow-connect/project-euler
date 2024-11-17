from numpy import zeros, sqrt
from math import ceil

n = 10001

def divisors(num):
	d = []
	for k in range(1, num // 2 + 1):
		if num // k * k == num:
			d.append(k)
	return d

sum_dividors = zeros(n)	

for num in range(1, n):
	d = divisors(num)
	if num == 220:
		print(d)
	if num == 284:
		print(d)	
	sum_dividors[num] = sum(d)

cnt = 0
for i in range(n):
	if sum_dividors[i] <= n:
		
		if sum_dividors[int(sum_dividors[i])] == i:
			cnt += i

#print(sum_dividors[220])
#print(sum_dividors[284])
print(cnt)
