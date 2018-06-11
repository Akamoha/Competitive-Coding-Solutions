import sys
import math
sys.setrecursionlimit(2147000000)
 
def findDivisors(n):
	list = []
	for i in range(1, int(math.sqrt(n)+1)):
		if n%i == 0:
			if n/i == i:
				div.append(i)
			else:
				div.append(i)
				list.append(n/i)
	div.extend(list[::-1])

def solve(N, C, U):
	if D[N] != 0:
		return 1
	if (N, C) in ht:
		return 0
	if N == 1:
		if C <= U:
			D[N] = C
			return 1
		ht[(N, C)] = 0
		return 0
	flag = False
	for divisor in div:
		i = divisor+N-1
		if i <= min(C+N-1, U):
			if C%divisor == 0:
				r = solve(N-1, C/divisor, i)
				if r == 1:
					flag = True
					break
		else:
			break
	if not flag:
		ht[(N, C)] = 0
		return 0
	D[N] = i
	return 1
 
for _ in xrange(input()):
	N, C = map(int, raw_input().split())
	D = [0 for __ in xrange(N+1)]
	div = []
	ht = {}
	findDivisors(C)
	solve(N, C, C+N-1)
	for i in xrange(1, N+1):
		print D[i],
	print