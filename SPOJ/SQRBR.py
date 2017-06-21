def solve(i, numOpen):
	if i == 1:
		if numOpen == 1:
			return 1
		return 0
	if (i, numOpen) not in ht:
		if opening[i] == 1:
			if numOpen == 0:
				ht[(i, numOpen)] = 0
			else:
				ht[(i, numOpen)] = solve(i-1, numOpen-1)
		elif numOpen == 0:
			ht[(i, numOpen)] = solve(i-1, 1)
		else:
			ht[(i, numOpen)] = solve(i-1, numOpen-1) + solve(i-1, numOpen+1)
	return ht[(i, numOpen)]

for _ in xrange(input()):
	n, k = map(int, raw_input().split())
	seq = map(int, raw_input().split())
	opening = [0 for i in xrange(2*n+1)]
	ht = {}
	for i in seq:
		opening[i] = 1
	print solve(2*n, 0)