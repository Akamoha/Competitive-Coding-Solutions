for _ in range(input()):
	N = input()
	s = 0.00
	for i in range(1, N+1):
		s += 1.0/i
	print "{:.2f}".format(s*N)