from heapq import *
def dijkstra(s):
	q, seen = [(0, s)], set()
	while q:
		cost, v1 = heappop(q)
		if v1 not in seen:
			seen.add(v1)
			SD[v1] = cost
			for c, v2 in g[v1]:
				if v2 not in seen:
					heappush(q, (cost+c, v2))
N = input()
g = [[] for _ in xrange(1000)]
SD = [-1 for _ in xrange(1000)]
for _ in xrange(N):
	A, B, W = map(int, raw_input().split())
	g[A].append((W, B))
	g[B].append((W, A))
U = input()
dijkstra(U)
Q = input()
for _ in xrange(Q):
	V = input()
	print SD[V] if SD[V] != -1 else "NO PATH"