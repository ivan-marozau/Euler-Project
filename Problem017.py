## Number letter counts
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

import time
start = time.clock()

def get_number_name(n):
	dic = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11 : 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'hundred', 1000: 'thousand'} 
	str = ''
	while n > 0:
		if n >= 1000:
			str = str + dic[n//1000] + dic[1000]
			n = n%1000
		elif n >= 100:
			str = str + dic[n//100] + dic[100]
			n = n%100
		else:
			if n > 20:
				str = str + dic[n//10*10] + dic[n%10]
				n = 0
			else:
				str = str + dic[n]
				n = 0
	return str

letter_count = 0
for i in range(1, 1001):
	letter_count += len(get_number_name(i))
		
print (letter_count + 99*9*3) # the latter is for 'and' in '... hundred and...'

end = time.clock()
print ("Running time: %s ms" % (end - start)/1000)
