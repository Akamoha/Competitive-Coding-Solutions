for _ in xrange(input()):
	L = input()
	S = raw_input()
	i = 0
	search = "HT"
	last = ''
	for s in S:
		if s == search[i]:
			i = 1-i
			last = s
		elif s == search[1-i]:
			print "Invalid"
			break
	else:
		if 'H' not in S and 'T' not in S:
			print "Valid"
		elif last == 'T':
			print "Valid"
		else:
			print "Invalid"