while True:
	N = raw_input()
	if N == "0":
		break
	DP = []
	for i in range(len(N)):
		DP.append(0)
	if len(N) == 1:
		print 1
		continue
	DP[0] = 1
	DP[1] = 1
	if int(N[0:2]) <= 26 and N[1] != '0':
		DP[1] = 2
	if N[1] == '0':
		if int(N[0]) >= 3:
			print 0
			continue
	for i in range(2, len(N)):
		if N[i] == '0':
			if N[i-1] == '0' or int(N[i-1]) >= 3:
				DP[len(N) - 1] = 0
				break
			DP[i] = DP[i-2]
		elif int(N[i-1:i+1]) <= 26:
			if N[i-1] != '0':
				DP[i] = DP[i-1] + DP[i-2]
			else:
				DP[i] = DP[i-1]
		else:
			DP[i] = DP[i-1]
	print DP[len(N) - 1]