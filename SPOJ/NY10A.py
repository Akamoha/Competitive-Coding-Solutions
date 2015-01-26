P = int(raw_input())
for _ in range(P):
	N = int(raw_input())
	sequence = raw_input()
	i = 0
	hashtable = {}
	while i+2 < len(sequence):
		subseq = sequence[i:i+3]
		if subseq in hashtable:
			hashtable[subseq] += 1
		else:
			hashtable[subseq] = 1
		i += 1
	print N,
	for subseq in ["TTT", "TTH", "THT", "THH", "HTT", "HTH", "HHT", "HHH"]:
		if subseq in hashtable:
			print hashtable[subseq],
		else:
			print 0,
	print