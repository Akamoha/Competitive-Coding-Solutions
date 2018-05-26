for _ in xrange(input()):
	n = input()
	A = map(int, raw_input().split())
	print ''.join(map(str, A))
	i, j = 0, 0
	for i in xrange(n-2, -1, -1):
		if A[i] < A[i+1]:
			break
	else:
		print "NO NXTBIG"
		continue
	mn = i+1
	for j in xrange(i+2, n):
		if A[mn] > A[j] and A[j] > A[i]:
			mn = j
	A[i], A[mn] = A[mn], A[i]
	B = A[i+1:]
	B.sort()
	A = A[:i+1] + B
	print ''.join(map(str, A))