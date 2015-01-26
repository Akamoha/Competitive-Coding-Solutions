for t in range(int(raw_input())):
	k = int(raw_input())
	A = [192,442,692,942]
	if k in range(5):
		print A[k-1]
	else:
		print str((k-1)/4)+str(A[(k%4)-1])