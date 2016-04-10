import math

def prime(a):
	if a <= 1:
		return -1
	for i in xrange(2, 8):
		if a % i == 0:
			return i
	return -1
	
for t in xrange(input()):
	N, J = map(int, raw_input().split())
	print "Case #"+str(t+1)+":"
	c = 0
	for i in xrange(100000):
		X = ('1'+format(i, '0'+str(N-2)+'b')+'1')[::-1]
		divisors = []
		for j in xrange(2, 11):
			num = 0
			ind = 0
			for s in X:
				num += int(s)*(j**ind)
				ind += 1
			res = prime(num)
			if res == -1:
				break
			divisors.append(res)
		else:
			print X[::-1],
			for divisor in divisors:
				print divisor,
			print
			c += 1
			if c >= J:
				break