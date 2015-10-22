def COMPUTE_PREFIX_FUNCTION(P):
	m = len(P) - 1
	pi = []
	for x in range(m+1):
		pi.append(0)
	pi[1] = 0
	k = 0
	for q in range(2, m+1):
		while k > 0 and P[k + 1] != P[q]:
			k = pi[k]
		if P[k + 1] == P[q]:
			k += 1
		pi[q] = k
	return pi
	

def KMP_MATCHER(T, P):
	n = len(T) - 1
	m = len(P) - 1
	pi = COMPUTE_PREFIX_FUNCTION(P)
	q = 0
	c = 0
	for i in range(1, n+1):
		while q > 0 and P[q + 1] != T[i]:
			q = pi[q]
		if P[q + 1] == T[i]:
			q += 1
		if q == m:
			c += 1
			print i - m
			q = pi[q]
	if c == 0:
		print

while True:
	try:
		n = input()
		P = " "+raw_input()			
		T = " "+raw_input()

		COMPUTE_PREFIX_FUNCTION(P)
		KMP_MATCHER(T, P)
		
		print
	except:
		break