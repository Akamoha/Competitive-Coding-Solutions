N = input()
R = map(int, raw_input().split())
HT = {}
for r in R:
	HT[r] = 1
for i in range(1, N+1):
	if i not in HT:
		print i,