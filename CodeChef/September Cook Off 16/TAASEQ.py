def isAP(A):
	D = A[1]-A[0]
	for i in xrange(2, len(A)):
		if A[i]-A[i-1] != D:
			return i
	return -1


for _ in xrange(input()):
	N = input()
	A = map(int, raw_input().split())
	if N == 2:
		print min(A)
	else:
		ind = isAP(A)
		if ind == -1:
			print min(A)
		else:
			ans = 10**9+7
			A1 = [x for x in A]
			A2 = [x for x in A]
			A3 = [x for x in A]
			A1.pop(ind-2)
			A2.pop(ind-1)
			A3.pop(ind)
			if isAP(A1) == -1:
				ans = min(ans, A[ind-2])
			if isAP(A2) == -1:
				ans = min(ans, A[ind-1])
			if isAP(A3) == -1:
				ans = min(ans, A[ind])
			if ans != 10**9+7:
				print ans
			else:
				print -1
			