from fractions import gcd
for _ in xrange(input()):
	N, M = map(int, raw_input().split())
	num = (N/2)*(M-(M/2)) + (M/2)*(N-(N/2))
	den = N*M
	gcdd = gcd(num, den)
	num /= gcdd
	den /= gcdd
	print str(num) + "/" + str(den)