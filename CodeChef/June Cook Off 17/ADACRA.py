for _ in xrange(input()):
	S, state, c = raw_input(), 'U', 0
	for s in S:
		if state == 'U' and s == 'D':
			state, c = 'D', c+1
		elif state == 'D' and s == 'U':
			state = 'U'
	state, c1 = 'D', 0
	for s in S:
		if state == 'D' and s == 'U':
			state, c1 = 'U', c1+1
		elif state == 'U' and s == 'D':
			state = 'D'
	print min(c, c1)