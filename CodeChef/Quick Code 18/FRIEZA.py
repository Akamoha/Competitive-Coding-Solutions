for _ in xrange(input()):
	S = raw_input()
	ans = ""
	i = 0
	while i < len(S):
		c = 0
		while i < len(S) and S[i] not in "frieza":
			c += 1
			i += 1
		if c != 0:
			ans += str(c)
		c = 0
		while i < len(S) and S[i] in "frieza":
			c += 1
			i += 1
		if c != 0:
			ans += str(c)
	print ans