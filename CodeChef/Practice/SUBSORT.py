for _ in xrange(input()):
	n = input()
	A = map(int, raw_input().split())
	if n == 1:
		print 1, 1
		continue
	L = [0 for _ in xrange(n)]
	R = [0 for _ in xrange(n)]
	mx = 0
	for i in xrange(n):
		if A[i] > mx:
			mx = A[i]
		L[i] = mx
	mn = 10**9+7
	for j in xrange(n-1, -1, -1):
		if A[j] < mn:
			mn = A[j]
		R[j] = mn
	i, j = 1, n-2
	while i < n and A[i-1] < A[i]:
		i += 1
	while j >= 0 and A[j] < A[j+1]:
		j -= 1
	if i > j:
		i, j = j, i
	mn = min(A[i:j+1])
	mx = max(A[i:j+1])
	if j+1 < n:
		mn = min(mn, R[j+1])
	while i-1 >= 0 and mn < L[i-1]:
		i -= 1
	while j+1 < n and mx > R[j+1]:
		j += 1
	if i+1 == 0:
		print "1,"+str(n)
	else:
		print str(i+1)+","+str(j+1)
	