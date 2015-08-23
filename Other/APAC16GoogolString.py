def findAns(K, cur):
	if K == 1:
		return 0
	x = 2**cur
	if K <= x/2 - 1:
		return findAns(K, cur-1)
	if K == x/2:
		return 0
	return 1 - findAns(x - K, cur-1)

for t in range(input()):
	K = input()
	print "Case #"+str((t+1))+": "+str(findAns(K, 60))