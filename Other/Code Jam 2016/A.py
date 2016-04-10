digits = [0 for _ in xrange(10)]

def updateDigits(L):
	for num in L:
		digits[int(num)] += 1

def allDigitsSeen():
	for num in xrange(10):
		if digits[num] == 0:
			return False
	return True

def solve(N):
	global digits
	if N == 0:
		return "INSOMNIA"
	digits = [0 for _ in xrange(10)]
	i = 1
	ori = N
	while True:
		updateDigits(list(str(N)))
		if allDigitsSeen():
			return N
		i += 1
		N = i*ori

for t in xrange(input()):
	N = input()
	print "Case #"+str(t+1)+": "+str(solve(N))