MOD = 1000000007

for _ in xrange(input()):
	p, q, r = map(int, raw_input().split())
	A = map(int, raw_input().split())
	B = map(int, raw_input().split())
	C = map(int, raw_input().split())
	A.sort()
	B.sort()
	C.sort()
	CSAX = []
	sumX = 0
	for i in xrange(p):
		sumX = (sumX+A[i])%MOD
		CSAX.append(sumX)
	CSAZ = []
	sumZ = 0
	for i in xrange(r):
		sumZ = (sumZ+C[i])%MOD
		CSAZ.append(sumZ)

	ans = 0
	Xi = 0
	Zi = 0
	for i in xrange(q):
		Y = B[i]
		if A[Xi] > Y or C[Zi] > Y:
			continue
		while Xi+1 < len(A) and A[Xi+1] <= Y:
			Xi += 1
		while Zi+1 < len(C) and C[Zi+1] <= Y:
			Zi += 1
		anspartA = ((Y*(Xi+1))%MOD + CSAX[Xi]%MOD)
		anspartB = ((Y*(Zi+1))%MOD + CSAZ[Zi]%MOD)
		ans =  (ans + ((anspartA%MOD)*(anspartB%MOD))%MOD)%MOD
	print ans