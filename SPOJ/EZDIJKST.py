from heapq import *
def dijkstra(s):
	q, seen = [(0,s)], set()
	while q:
		cost, v1 = heappop(q)
		if v1 not in seen:
			seen.add(v1)
			shortestDistance[v1] = cost
			for c, v2 in g[v1]:
				if v2 not in seen:
					heappush(q, (cost+c, v2))
for _ in range(input()):
	V, K = map(int, raw_input().split())
	g = [[] for _ in xrange(V+1)]
	shortestDistance = [-1 for _ in xrange(V+1)]
	for k in xrange(K):
		a, b, c = map(int, raw_input().split())
		g[a].append((c, b))
	A, B = map(int, raw_input().split())
	dijkstra(A)
	print "NO" if shortestDistance[B] == -1 else shortestDistance[B]