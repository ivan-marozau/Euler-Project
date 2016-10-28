## 10001st prime
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

import time
start = time.clock()

def prime_index(n):
	lst = [2]
	x = 3
	while len(lst) < n:
		i = 0
		while lst[i]**2 <= x:
			if x%lst[i] == 0:
				break
			else:
				i += 1
		if lst[i]**2 > x:
			lst.append(x)
		else:
			pass
		x += 2
	return lst[-1]
	
print (prime_index(10001))
		
end = time.clock()
print ("Running time: %s seconds" % (end - start))
