## 10001st prime
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

import time
start = time.clock()

def isPrime(n):
	if n == 1: return False
	elif n < 4: return True
	elif n%2 == 0: return False
	elif n < 9: return True
	elif n%3 == 0: return False
	else:
		f = 5
		while f*f <= n:
			if n%f == 0 or n%(f+2) == 0:
				return False
				break
			else: f+=6
		return True

def prime_index(limit):
	count = 1
	candidate = 1
	while count < limit:
		candidate += 2
		if isPrime(candidate):
			count += 1
	return candidate
	
print (prime_index(100001))
		
end = time.clock()
print ("Running time: %s seconds" % (end - start))
