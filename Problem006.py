## Sum square difference
# The sum of the squares of the first ten natural numbers is 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import time
start = time.clock()

def sq_of_sum(n):
	return (n*(n+1)/2)**2
	
def sum_of_sqs(n):
	return (n*(n+1)*(2*n+1))/6
	
def diff_sqs(n):
	return int(sq_of_sum(n) - sum_of_sqs(n))

n = int(input('Enter the value: '))	
print (diff_sqs(n))
		
end = time.clock()
print ("Running time: %s ms" % round((end - start)*1000))
