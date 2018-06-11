for _ in xrange(input()):
	n = input()
	a = map(int, raw_input().split())
	print n - max(a)