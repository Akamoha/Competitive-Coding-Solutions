def solve(S):
	curr = S[0]
	count = 0
	for s in S:
		if s != curr:
			curr = s
			count += 1
	if (S[0], S[-1]) == ('+', '+'):
		return count
	if (S[0], S[-1]) == ('+', '-'):
		return count+1
	if (S[0], S[-1]) == ('-', '+'):
		return count
	if (S[0], S[-1]) == ('-', '-'):
		return count+1

for t in xrange(input()):
	S = raw_input()
	print "Case #"+str(t+1)+": "+str(solve(S))