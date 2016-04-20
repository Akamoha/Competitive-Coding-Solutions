T = input()
for _ in xrange(T):
	blank = raw_input()
	m, n = map(int, raw_input().split())
	cuts = []
	for _ in xrange(m-1):
		cuts.append((input(), 'H'))
	for _ in xrange(n-1):
		cuts.append((input(), 'V'))
	cuts.sort(reverse=True)
	h, v, ans = 0, 0, 0
	for cut in cuts:
		if cut[1] == 'H':
			h += 1
			ans += (v+1)*cut[0]
		else:
			v += 1
			ans += (h+1)*cut[0]
	print ans