for _ in xrange(input()):
	s = raw_input()
	ans = 0
	cur = 0
	for i in xrange(len(s)):
		if s[i] == '>':
			cur -= 1
		else:
			cur += 1
		if cur < 0:
			break
		if cur == 0:
			ans = max(ans, i+1)
	print ans