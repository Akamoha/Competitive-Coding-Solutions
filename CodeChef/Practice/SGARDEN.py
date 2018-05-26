from fractions import gcd
MOD = 10**9 + 7

def lcm(a, b):
	return a*b/gcd(a, b)

def findCycleSize(i):
	cycleSize = 1
	j = A[i]
	while j != i:
		visited[j] = 1
		cycleSize += 1
		j = A[j]
	return cycleSize

for _ in xrange(input()):
	N = input()
	A = [0]+map(int, raw_input().split())
	visited = [0 for _ in xrange(N+1)]
	cycles = []
	for i in xrange(1, N+1):
		if visited[i] == 0:
			cycles.append(findCycleSize(i))
	totalCycles = len(cycles)
	print reduce(lcm, cycles)%MOD