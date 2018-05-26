def merge(A, B):
	global inv
	i, j = 0, 0
	C = []
	while i < len(A) and j < len(B):
		if A[i] < B[j]:
			C.append(A[i])
			i += 1
		else:
			C.append(B[j])
			j += 1
			inv += len(A)-i
	C.extend(A[i:])
	C.extend(B[j:])
	return C

def mergeSort(A):
	if len(A) < 2:
		return A
	m = len(A)/2
	return merge(mergeSort(A[:m]), mergeSort(A[m:]))
	
N, Q = map(int, raw_input().split())
A = map(int, raw_input().split())
inv = 0
mergeSort(A)
inv %= 2

for q in xrange(Q):
	X, Y = map(int, raw_input().split())
	inv = 1-inv
	print inv