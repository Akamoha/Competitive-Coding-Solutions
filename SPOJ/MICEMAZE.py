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
N = input()
E = input()
T = input()
M = input()
g = [[] for _ in xrange(N+1)]
for m in xrange(M):
	a, b, w = map(int, raw_input().split())
	g[b].append((w, a))
shortestDistance = [-1 for _ in xrange(N+1)]
dijkstra(E)
ans = 0
for n in xrange(1, N+1):
	if shortestDistance[n] != -1 and shortestDistance[n] <= T:
		ans += 1
print ans