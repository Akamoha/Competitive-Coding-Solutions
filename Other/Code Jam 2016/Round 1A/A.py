for t in xrange(input()):
	S = list(raw_input())
	answer = S[0]
	for s in S[1:]:
		if s < answer[0]:
			answer += s
		else:
			answer = s+answer
	print "Case #"+str(t+1)+":",answer