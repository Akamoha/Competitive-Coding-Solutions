def f(A, x, C):
	prev = A[0]
	cowsplaced = 1
	for i in range(1, len(A)):
		if A[i] - prev >= x:
			cowsplaced += 1
			if cowsplaced == C:
				return 1
			prev = A[i]
	return 0

for _ in range(input()):
	N, C = map(int, raw_input().split())
	A = []
	for i in range(N):
		A.append(input())
	A.sort()
	low, high = 0, A[N-1]
	while low < high:
		mid = (low + high)/2
		if f(A, mid, C) == 0:
			high = mid
		else:
			low = mid + 1
	print low - 1