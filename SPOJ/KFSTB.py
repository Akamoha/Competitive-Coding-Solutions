import sys
sys.setrecursionlimit(2147000000)

def solve(s, p):
	if s in memo:
		return memo[s]
	if len(g[s]) == 0:
		if s == T:
			return 1
		return 0
	res = 0
	for node in g[s]:
		if node != p:
			res = (res+solve(node, s))%MOD
	memo[s] = res
	return res

MOD = 10**9+7
for _ in xrange(input()):
	C, B, S, T = map(int, raw_input().split())
	g = [[] for _ in xrange(C+1)]
	memo = {}
	for _ in xrange(B):
		X, Y = map(int, raw_input().split())
		g[X].append(Y)
	print solve(S, 0)