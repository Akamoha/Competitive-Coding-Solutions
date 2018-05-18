from math import sqrt
for _ in xrange(input()):
	B, LS = map(int, raw_input().split())
	Bsq = pow(B, 2)
	LSsq = pow(LS, 2)
	mxRS = sqrt(Bsq + LSsq)
	mnRS = sqrt(LSsq - Bsq)
	print mnRS, mxRS