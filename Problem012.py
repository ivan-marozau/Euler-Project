## Highly divisible triangular number
# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# Let us list the factors of the first seven triangle numbers:
#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.
# What is the value of the first triangle number to have over five hundred divisors?

import time
start = time.clock()

def triangle(n):
	return n*(n+1)//2

def numFactors(n):
	a = 2*sum([1 for i in range(1,int(n**0.5)+1) if n % i == 0])
	if n**0.5 == int(n**0.5):
		return a - 1
	else:
		return a

num = 1
a = 0
while numFactors(a) < 500:
	a = triangle(num)
	num += 1
print (a)

end = time.clock()
print ("Running time: %s seconds" % (end - start))
