T = int(raw_input())
for _ in range(T):
	N = int(raw_input())
	A = map(int, raw_input().split())
	A.sort(reverse = True)
	count = 0
	i = 0
	if N == 1:
		print A[0]
	elif N%2 == 0:
		while i < N:
			count += (A[i] + A[i+1])
			i += 4
		print count
	elif (N-1) % 4 == 0:
		while i < N-1:
			count += (A[i] + A[i+1])
			i += 4
		count += A[-1]
		print count
	else:
		while i < N:
			count += (A[i] + A[i+1])
			i += 4
		print count