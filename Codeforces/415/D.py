MOD = 10**9+7

def sum(a, b):
	return (a+b)%MOD

n, k = map(int, raw_input().split())

DP = [[]]
DP.append([0] + [1 for i in xrange(1, n+1)])

factors = {}
for i in xrange(1, n+1):
	factors[i] = []
	for j in xrange(1, i+1):
		if i%j == 0:
			factors[i].append(j)

for i in xrange(2, k+1):
	DP.append([0 for _ in xrange(n+1)])
	for j in xrange(1, n+1):
		for f in factors[j]:
			DP[i][j] = (DP[i][j] + DP[i-1][f])%MOD

print reduce(sum, DP[k])