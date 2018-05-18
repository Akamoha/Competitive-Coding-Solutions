def display(A):
	for a in A:
		print a,
	print

N, K = map(int, raw_input().split())
A = map(int, raw_input().split())
if K == 0:
	display(A)
else:
	mxA = max(A)
	B = [mxA-x for x in A]
	if K%2 == 1:
		display(B)
	else:
		mxB = max(B)
		display([mxB-x for x in B])