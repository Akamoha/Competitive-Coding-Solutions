T = int(raw_input())
for _ in range(T):
	N = int(raw_input())
	A = map(int, raw_input().split())
	HT = {}
	max = 1
	for a in A:
		if a not in HT:
			HT[a] = 1
		else:
			HT[a] += 1
			if HT[a] > max:
				max = HT[a]
	print (N-max)
	
	