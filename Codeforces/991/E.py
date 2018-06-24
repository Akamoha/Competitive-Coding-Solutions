import operator

def factorial(x):
	if x == 0:
		return 1
	return x*factorial(x-1)

n = map(int, list(raw_input()))
HT = [0 for _ in xrange(10)]
for d in n:
	HT[d] += 1
discount = [0 for _ in xrange(10)]
for d in xrange(10):
	if HT[d] == 0:
		HT[d] = discount[d] = 1
ans = 0
for i0 in xrange(1, HT[0]+1):
	for i1 in xrange(1, HT[1]+1):
		for i2 in xrange(1, HT[2]+1):
			for i3 in xrange(1, HT[3]+1):
				for i4 in xrange(1, HT[4]+1):
					for i5 in xrange(1, HT[5]+1):
						for i6 in xrange(1, HT[6]+1):
							for i7 in xrange(1, HT[7]+1):
								for i8 in xrange(1, HT[8]+1):
									for i9 in xrange(1, HT[9]+1):
										nums = [i0, i1, i2, i3, i4, i5, i6, i7, i8, i9]
										nondiscounted = [nums[d] for d in xrange(10) if discount[d] != 1]
										s = sum(nondiscounted)
										ans += factorial(s)/reduce(operator.mul, [factorial(x) for x in nondiscounted], 1)
										if discount[0] == 0:
											nondiscounted = [nums[0]-1]+[nums[d] for d in xrange(1, 10) if discount[d] != 1]
											ans -= factorial(s-1)/reduce(operator.mul, [factorial(x) for x in nondiscounted], 1)
print ans