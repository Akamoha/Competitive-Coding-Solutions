while True:
	n = input()
	if n == 0:
		break
	A = []
	for i in range(n):
		A.append(input())
	A.sort()
	for i in range(1, len(A)):
		if A[i] - A[i-1] > 200:
			print "IMPOSSIBLE"
			break
	else:
		if 1422 - A[-1] > 100:
			print "IMPOSSIBLE"
		else:
			for i in range(len(A)-1, 0, -1):
				if A[i] - A[i-1] > 200:
					print "IMPOSSIBLE"
					break
			else:
				print "POSSIBLE"