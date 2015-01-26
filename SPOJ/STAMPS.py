T = int(raw_input())
for t in range(T):
	numStamps, numFriends = map(int, raw_input().split())
	stamps = map(int, raw_input().split())
	stamps.sort()
	s = 0
	i = 0
	for n in stamps[::-1]:
		i += 1
		s += n
		if s >= numStamps:
			print "Scenario #"+str(t+1)+":"
			print i
			print
			break
	else:
		print "Scenario #"+str(t+1)+":"
		print "impossible"