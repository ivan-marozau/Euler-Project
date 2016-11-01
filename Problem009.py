# Special Pythagorean triplet
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import time
start = time.clock()

def pyttri_prd(sum):
	n = 0
	for a in range(3, int(sum/3)):
		for b in range (a+1, int((sum-a)/2)):
			for c in range(b+1, sum-(a+b)):
				if c*c == a*a + b*b and sum%(a+b+c) == 0:
					n = a*b*c*(sum//(a+b+c))**3
					break
			if n != 0:
				break
		if n != 0:
			break
	return n
	
print (pyttri_prd(1000))

end = time.clock()
print ("Running time: %s seconds" % (end - start))
