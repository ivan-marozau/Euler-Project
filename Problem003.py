## Largest prime factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import time

def c_range(n):
    cur = 5
    incr = 2
    while cur < n+1:
        yield cur
        cur += incr
        incr = 6 - incr

def sieve(end):
    primes_lst = [2, 3]
    sieve_lst = [True] * (end+1)
    for num in c_range(end):
        if sieve_lst[num]:
            primes_lst.append(num)
            for multiple in range(num**2, end+1, num):
                sieve_lst[multiple] = False
    return primes_lst

def lpf_sieve(n):
	if n == 1: return None
	while n%2 == 0:
		n = n//2
	if n == 1: return 2
	i = 0
	lst = sieve(int(n**0.5)+1)
	while i < len(lst) and lst[i] < n:
		if n%lst[i] == 0:
			n = n//lst[i]
		else:
			i += 1
		if i == len(lst):
			return n
	return lst[i]

def lpf(n):
	if n == 1: return None
	while n%2 == 0:
		n //= 2
	if n == 1: return 2
	i = 3
	while i <= n:
		if n%i == 0:
			n = n//i
		else:
			i += 2
		if i > 10000:
			return lpf_sieve(n)
	return i
	
initial_number = int(input('Enter the number:\n'))
n = initial_number

start = time.clock()
lpf = lpf(n)
end = time.clock()

if initial_number == lpf:
	print ("%s is prime." % lpf)
else:
	print ("The largest prime factor of %s is %s." % (initial_number, lpf))
	
print ("Running time: %s ms" % round((end - start)*10**3))
