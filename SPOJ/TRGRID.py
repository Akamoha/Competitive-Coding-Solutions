NM = {1: 'D', 0: 'U'}
MN = {1: 'R', 0: 'L'}
for _ in range(input()):
	N, M = map(int, raw_input().split())
	if N > M:
		print NM[M%2]
	else:
		print MN[N%2]