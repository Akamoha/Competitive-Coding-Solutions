"""
This is the knapsack-type DP solution that gives TLE
"""
def solve(i, last):
	if i == n:
		return 0
	if(i, last) in memo:
		return memo[(i, last)]
	if C[i][1] < last:
		x = solve(i+1, last)
		memo[(i, last)] = x
		return x
	else:
		x = max(solve(i+1, last), 1+solve(i+1, C[i][1]))
		memo[(i, last)] = x
		return x

for _ in xrange(input()):
	n = input()
	A = map(int, raw_input().split())
	B = map(int, raw_input().split())
	C = [(A[i], B[i]) for i in xrange(n)]
	C.sort()
	memo = {}
	print max(solve(1, 0), 1+solve(1, C[0][1]))