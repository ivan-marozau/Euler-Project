## Summation of primes
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import time
start = time.clock()

def sum_of_primes(n):
	lst = list(range(n))
	lst[1] = 0
	i = 2
	while i*i < n:
	    if lst[i] != 0:
	        for j in range(i*2, n, i):
	            lst[j] = 0
	    i += 1
	return sum(lst)

print (sum_of_primes(2*10**6))	

end = time.clock()
print ("Running time: %s seconds" % (end - start))
