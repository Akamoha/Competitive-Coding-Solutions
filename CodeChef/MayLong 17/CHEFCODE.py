N, K = map(int, raw_input().split())
A = map(int, raw_input().split())
C = 0

def doyathang(prod, i):
	global C
	if i == N:
		return
	if prod*A[i] > K:
		C += 2**(N-i-1)
	else:
		doyathang(A[i]*prod, i+1)
	doyathang(prod, i+1)
	
doyathang(1, 0)
print 2**N - 1 - C