for t in range(int(raw_input())):
	s = raw_input()
	N = int(raw_input())
	count = 0
	for i in range(N):
		count += int(raw_input())
	print "YES" if count % N == 0 else "NO"