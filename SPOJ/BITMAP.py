from heapq import *

def canBeVisited(node):
	x, y = node
	if x < 0 or y < 0 or x >= n or y >= m:
		return False
	if visited[x][y] != -1:
		return False
	return True

def adjList(node):
	x, y = node
	return [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]

for _ in xrange(input()):
	n, m = map(int, raw_input().split())
	A = []
	q = []
	visited = []
	for i in xrange(n):
		A.append(raw_input())
		visited.append([-1 for _ in xrange(m)])
	for i in xrange(n):
		for j in xrange(m):
			if A[i][j] == '1':
				heappush(q, (0, (i, j)))
	while q:
		dist, v1 = heappop(q)
		x, y = v1
		if visited[x][y] == -1:
			visited[x][y] = dist
			for node in adjList(v1):
				if canBeVisited(node):
					heappush(q, (dist+1, node))
	for i in xrange(n):
		for j in xrange(m):
			print visited[i][j],
		print
	blank = raw_input()