memo = []

def solve(l, r):
	if memo[l][r-1] != -1:
		return memo[l][r-1]
	if l+1 == r:
		memo[l][r-1] = 0
		return 0
	cost = 10000000000
	for i in range(l+1, r):
		c = solve(l, i) + solve(i, r) + (sum(A[l:i])%100)*(sum(A[i:r])%100)
		if c < cost:
			cost = c
	memo[l][r-1] = cost
	return cost
	

while True:
	try:
		n = input()
		memo = []
		for i in range(n):
			zeros = []
			for j in range(n):
				zeros.append(-1)
			memo.append(zeros)
		A = map(int, raw_input().split())
		print solve(0, len(A))
	except:
		break