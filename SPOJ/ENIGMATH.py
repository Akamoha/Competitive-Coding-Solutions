from fractions import gcd
for _ in range(input()):
	A, B = map(int, raw_input().split())
	x = gcd(A, B)
	print B/x, A/x