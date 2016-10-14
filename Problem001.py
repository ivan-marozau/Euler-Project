## Multiples of 3 and 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

import time
start = time.clock()

def SumOfMultiples(target, div):
	n = target//div
	return div*(n*(n+1))//2
	
def SumOfMultiples_2(target, div1, div2):
	return SumOfMultiples(target, div1) + SumOfMultiples(target, div2) - SumOfMultiples(target, div1*div2)

print (SumOfMultiples_2(999,3,5))

end = time.clock()
print ("Running time: %s seconds" % (end - start))
