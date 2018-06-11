while True:
	H, W = map(int, raw_input().split())
	if [H, W] == [-1, -1]:
		break
	N = input()
	HT = {}
	for _ in xrange(N):
		x, y, d = map(int, raw_input().split())
		start = max(1, y-d)
		end = min(H, y+d)
		if start not in HT:
			HT[start] = 0
		if end not in HT:
			HT[end] = 0
		HT[start] += 1
		HT[end] -= 1
	on = 0
	maxon = 0
	for key in sorted(HT):
		on += HT[key]
		maxon = max(maxon, on)
	print maxon