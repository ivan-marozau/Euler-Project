## Smallest multiple
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import time
start = time.clock()

def prime_factors(n):
	lst = []
	i = 2
	count = 1
	while i <= n:
		if n%i == 0:
			n = n/i
			lst.append(i)
		else:
			i += 1
	return lst
# returns a list of all the prime factors of number n
	
def count(lst): 
	keys = sorted(list(set(lst)))
	values = []
	for i in keys:
		values.append(lst.count(i))
	d = dict(zip(keys,values))
	return d
# returns a dictionary, where the keys are the elements of the list, and the values are the number of occurrences of each element in the list

def lcm(n):
	lcm_dict = {}
	for i in range(n, 1, -1):
		for prime in count(prime_factors(i)):
			if prime not in lcm_dict or count(prime_factors(i))[prime] > lcm_dict[prime]:
				lcm_dict.update({prime: count(prime_factors(i))[prime]})
			else:
				pass
# creates a consolidated dictionary of prime factors for all numbers in the range
	result = 1
	for prime in lcm_dict:
		result = result*(int(prime)**int(lcm_dict[prime]))
# counts Least Common Multiple
	return result
	
print (lcm(20))
		
end = time.clock()
print ("Running time : %s seconds" % (end - start))
