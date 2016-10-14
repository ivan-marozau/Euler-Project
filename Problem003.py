## Largest prime factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import time
start = time.clock()

def lpf(n):
	if n%2 == 0:
		lastFactor = 2
		n = n//2
		while n%2 == 0:
	 		n=n//2
	else:
		lastFactor=1
		factor=3
	while n>1 and factor**2 <= n:
	 	if n%factor==0:
	 		n=n//factor
	 		lastFactor=factor
	 		while n%factor==0:
	 			n=n//factor
	 	factor=factor+2
	if n==1:
		return lastFactor
	else:
		return n
	
print (lpf(600851475143))

end = time.clock()
print ("Running time: %s seconds" % (end - start))
