def broken(N):
	sum = 0
	while N > 0:
		digit = N%10
		N = N/10
		sum = sum + digit**2
	return sum

N = int(raw_input())
A = {}
count = 0
while True:
	count += 1
	N = broken(N)
	if N in A:
		print "-1"
		break
	elif N == 1:
		print count
		break
	A[N] = 1