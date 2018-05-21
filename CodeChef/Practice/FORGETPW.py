for _ in xrange(input()):
	N = input()
	HT = {}
	for __ in xrange(N):
		c, p = raw_input().split()
		HT[c] = p
	S = raw_input()
	ans = ""
	for c in S:
		if c not in HT:
			HT[c] = c
		ans += HT[c]
	i, j = 0, len(ans)-1
	while i < j and ans[i] == '0':
		i += 1
	if '.' in ans:
		while j > i and ans[j] == '0':
			j -= 1
		if ans[j] == '.':
			j -= 1
	if i == j+1:
		print "0"
	else:
		print ans[i:j+1]