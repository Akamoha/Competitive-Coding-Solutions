import math as m
while True:
	A = map(int, raw_input().split())
	if A == [-1]*8:
		break
	maxi = int(max([m.ceil(1.0*A[i]/A[i+4]) for i in range(4)]))
	for i in range(4):
		print maxi*A[i+4] - A[i],
	print
