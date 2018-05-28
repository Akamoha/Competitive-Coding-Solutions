n, k = map(int, raw_input().split())
if k == 0:
	print 1 if n == 1 else -1
elif n == 1 or n/2 > k:
	print -1
elif n/2 == k:
	for i in xrange(1, n+1):
		print i,
	print
else:
	x = k-(n-2)/2
	print x, 2*x,
	for i in xrange(2*x+1, 2*x+1+n-2):
		print i,
	print