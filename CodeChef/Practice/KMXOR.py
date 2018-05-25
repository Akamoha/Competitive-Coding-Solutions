import math

for _ in xrange(input()):
	N, K = map(int, raw_input().split())
	if N == 1:
		print K
		continue
	if K == 1:
		for i in xrange(N):
			print 1,
		print
	elif K == 2:
		print 2,
		for i in xrange(N-1):
			print 1,
		print
	elif K == 3:
		if N%2 == 1:
			print 3,
			for i in xrange(N-1):
				print 1,
			print
		else:
			print 2,
			for i in xrange(N-1):
				print 1,
			print
	else:
		x = pow(2, int(math.log(K, 2)))
		if N%2 == 1:
			print x, x-2,
			for i in xrange(N-2):
				print 1,
			print
		else:
			print x, x-1,
			for i in xrange(N-2):
				print 1,
			print