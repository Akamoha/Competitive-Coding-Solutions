for _ in range(input()):
	S = raw_input()
	print "YES" if S == S[::-1] else "NO"