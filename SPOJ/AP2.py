for _ in range(input()):
	x, y, s = map(int, raw_input().split())
	n = 2*s/(x+y)
	print n
	d = (x-y)/(5-n)
	a1 = x - 2*d
	for i in range(1, n+1):
		print a1 + (i-1)*d,
	print