def numRecur(N):
	if N == 1:
		return 1
	else:
		return numRecur(N-1) + 2*N - 1 + (N-1)**2

while True:
	N = int(raw_input())
	if N == 0:
		break
	else:
		print numRecur(N)