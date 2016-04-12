import sys
sys.setrecursionlimit(1000000)

memo = {}

def solve(H, A, state):
	if(H,A,state) in memo:
		return memo[(H,A,state)]
	if H <= 0 or A <= 0:
		return -1
	if state == 1:
		answer = 1+max(solve(H-20, A+5, 2), solve(H-5, A-10, 3))
		memo[(H,A,state)] = answer
		return answer
	if state == 2:
		answer = 1+max(solve(H+3, A+2, 1), solve(H-5, A-10, 3))
		memo[(H,A,state)] = answer
		return answer
	answer = 1+max(solve(H+3, A+2, 1), solve(H-20, A+5, 2))
	memo[(H,A,state)] = answer
	return answer

for _ in xrange(input()):
	H, A = map(int, raw_input().split())
	print max(solve(H, A, 1), solve(H, A, 2), solve(H, A, 3))