## Largest prime factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import time

def sieve(n):
    check_lst = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if check_lst[i//2]:
            check_lst[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if check_lst[i]]

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
	
initial_number = 600851475145 #int(input('Enter the number:\n'))
n = initial_number

start = time.clock()
lpf = lpf(n)
end = time.clock()

if initial_number == lpf:
	print ("%s is prime." % lpf)
else:
	print ("The largest prime factor of %s is %s." % (initial_number, lpf))
	
print ("Running time: %s ms" % round((end - start)*10**3))
