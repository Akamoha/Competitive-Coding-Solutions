from collections import deque
visited = {}
def DFS(s):
	global visited
	visited[s] = 1
	print s, 
	for v1 in g[s]:
		if v1 not in visited:
			DFS(v1)

def BFS(s):
	q = deque()
	q.append(s)
	visited = {}
	visited[s] = 1
	while q:
		v1 = q.popleft()
		print v1,
		for node in g[v1]:
			if node not in visited:
				visited[node] = 1
				q.append(node)

for t in range(input()):
	n = input()
	g = [[] for _ in xrange(n+1)]
	for i in xrange(1, n+1):
		s = raw_input().split(" ")
		s = [int(x) for x in s]
		g[i] = s[2:]
	print "graph", t+1
	v, i = map(int, raw_input().split())
	while v != 0 or i != 0:
		if i == 0:
			visited = {}
			DFS(v)
			print 
		else:
			BFS(v)
			print 
		v, i = map(int, raw_input().split())