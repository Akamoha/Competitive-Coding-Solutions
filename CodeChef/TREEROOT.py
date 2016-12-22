for _ in xrange(input()):
	N = input()
	ans = 0
	for __ in xrange(N):
		a, b = map(int, raw_input().split())
		ans += a-b
	print ans