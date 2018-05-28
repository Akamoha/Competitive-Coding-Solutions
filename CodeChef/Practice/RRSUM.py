N, M = map(int, raw_input().split())
mn, mx = 2+N, 3*N
mid = (mn+mx)/2
for _ in xrange(M):
	q = input()
	if q < mn or q > mx:
		print 0
	elif q <= mid:
		print q-mn+1
	else:
		print mx-q+1