MAX = 10**6

numFactors = [0 for _ in xrange(MAX+1)]

for i in xrange(2, MAX+1):
	if numFactors[i] == 0:
		for j in xrange(i, MAX+1, i):
			numFactors[j] += 1

for _ in xrange(input()):
	n, m = map(int, raw_input().split())
	print sum(numFactors[n:m])