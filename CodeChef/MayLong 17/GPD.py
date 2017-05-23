from collections import deque

MAX = 2**31 - 1
MIN = 0

def solve(v, k):
	a = MAX
	b = MIN
	while v != -1:
		xor = key[v]^k	
		if xor < a:
			a = xor
		if xor > b:
			b = xor
		v = parent[v]
	return [a, b]

N, Q = map(int, raw_input().split())
R, k = map(int, raw_input().split())
key = {}
key[R] = k
parent = {}
parent[R] = -1
for _ in xrange(N-1):
	u, v, k = map(int, raw_input().split())
	key[u] = k
	parent[u] = v

last = 0

for _ in xrange(Q):
	q = map(int, raw_input().split())
	for i in xrange(len(q)):
		q[i] = q[i]^last
	if q[0] == 0:
		parent[q[2]] = q[1]
		key[q[2]] = q[3]
	else:
		a, b = solve(q[1], q[2])
		last = a^b
		print a, b