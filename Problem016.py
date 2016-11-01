## Power digit sum
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?
import time
start = time.clock()

def sum_of_digits(n):
	return sum([int(i) for i in str(n)])
	
print (sum_of_digits(2**1000))

end = time.clock()
print ("Running time: %s seconds" % (end - start))
