n = int(raw_input())
while n != 0:
	A = map(int, raw_input().split())
	i = 0
	for num in A:
		if A[num-1] != (i+1):
			print "not ambiguous"
			break
		i += 1
	else:
		print "ambiguous"
	n = int(raw_input())