# There don't seem to be any AC submissions for D-query in Python/PyPy
# Just keeping this as a Python template for Mo's algorithm

import math

MAX = 10**6+1

def greater(a, b):
	global rootn
	if a[0]/rootn > b[0]/rootn:
		return 1
	elif a[0]/rootn == b[0]/rootn:
		return a[1] > b[1]
	return -1

def solve(l, r):
	global start
	global end
	global c
	while end < r:
		end += 1
		freq[A[end]] += 1
		if freq[A[end]] == 1:
			c += 1
	while end > r:
		freq[A[end]] -= 1
		if freq[A[end]] == 0:
			c -= 1
		end -= 1
	while start < l:
		freq[A[start]] -= 1
		if freq[A[start]] == 0:
			c -= 1
		start += 1
	while start > l:
		start -= 1
		freq[A[start]] += 1
		if freq[A[start]] == 1:
			c += 1
	return c

n = input()
A = [0]+map(int, raw_input().split())
q = input()
Q = []
for k in xrange(q):
	i, j = map(int, raw_input().split())
	Q.append((i, j, k))
	
rootn = math.sqrt(n)
Q = sorted(Q, cmp=greater)

c = 1
freq = [0 for _ in xrange(MAX+1)]
ans = [0 for _ in xrange(q)]
start = end = Q[0][0]
freq[A[start]] = 1
for query in Q:
	ans[query[2]] = solve(query[0], query[1])
	
for i in xrange(q):
	print ans[i]