import math
import itertools as it

def primeFactorize(n):
	l = {}
	while n%2 == 0:
		if 2 not in l:
			l[2] = 0
		l[2] += 1
		n /= 2
	for i in xrange(3, int(math.sqrt(n))+1, 2):
		while n%i == 0:
			if i not in l:
				l[i] = 0
			l[i] += 1
			n /= i
	if n > 2:
		l[n] = 1
	return l
	
l, r, G, L = map(int, raw_input().split())
if L%G != 0:
	print 0
else:
	p = primeFactorize(L/G)
	ans = 0
	cons = {}
	for i in xrange(len(p)+1):
		for combo in it.combinations(p.keys(), i):
			A = 1
			for j in combo:
				A *= j**p[j]
			B = (L/G)/A
			A, B = min(A, B), max(A, B)
			if A == B:
				if A in cons:
					continue
				cons[A] = 1
			if A*G >= l and B*G <= r:
				ans += 1
	print ans