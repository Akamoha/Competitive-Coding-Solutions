import math

for _ in xrange(input()):
	N = input()
	l = int(math.log(N)/math.log(2))
	print min(abs(2**l - N), abs(2**(l+1) - N), abs(2**(l-1) - N)) 
