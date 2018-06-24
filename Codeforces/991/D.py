A=[list(raw_input())]
A.append(list(raw_input()))
bishwocks = 0
for i in xrange(len(A[0])-1):
	if A[0][i] == A[1][i] == A[1][i+1] == '0':
		A[0][i] = A[1][i] = A[1][i+1] = 'X'
		bishwocks += 1
	elif A[0][i] == A[1][i] == A[0][i+1] == '0':
		A[0][i] = A[1][i] = A[0][i+1] = 'X'
		bishwocks += 1
	elif A[0][i] == A[0][i+1] == A[1][i+1] == '0':
		A[0][i] = A[0][i+1] = A[1][i+1] = 'X'
		bishwocks += 1
	elif A[1][i] == A[1][i+1] == A[0][i+1] == '0':
		A[1][i] = A[1][i+1] = A[0][i+1] = 'X'
		bishwocks += 1
print bishwocks