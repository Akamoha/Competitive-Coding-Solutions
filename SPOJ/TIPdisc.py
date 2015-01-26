T = int(raw_input())
for t in range(T):
	N,X = map(int, raw_input().split())
	S = map(int, raw_input().split())
	S.sort()
	j = 0
	i = len(S)-1
	disknum = 0
	while j <= i:
		if j < i and S[i] + S[j] <= X:
			j += 1
		i -= 1
		disknum += 1
	print "Case #"+str(t+1)+": "+str(disknum)