## Sum square difference
# The sum of the squares of the first ten natural numbers is 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import time
start = time.clock()

def diff_sqs(n):
	x, y = 0, 0
	for i in range(1, n+1):
		x += i
		y += i**2
	return (x*x)-y
	
print (diff_sqs(100))
		
end = time.clock()
print ("Running time: %s seconds" % (end - start))
