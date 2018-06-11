a, b = 0, 0
 
def inp():
	return map(int, raw_input().split())
 
def DFS(i, j):
	global a
	global b
	sz = 0
	stack = [(i, j)]
	while len(stack) > 0:
		u, v = stack.pop()
		if (a, b) not in visited[u][v]:
			visited[u][v][(a, b)] = 1
			sz += 1
			for x, y in adj[u][v]:
				if A[x][y] in [a, b]:
					if (a, b) not in visited[x][y]:
						stack.append((x, y))
	return sz
	
def solve(i, j):
	global a
	global b
	size = 0
	flowers = {}
	for x, y in adj[i][j]:
		flowers[A[x][y]] = 1
	for f in flowers:
		mn, mx = min(A[i][j], f), max(A[i][j], f)
		if (mn, mx) not in visited[i][j]:
			a, b = mn, mx
			size = max(size, DFS(i, j))
	return size
 
n, m = inp()
A = []
for _ in xrange(n):
	A.append(inp())
 
adj = []
for i in xrange(n):
	adj.append([])
	for j in xrange(m):
		adj[i].append([])
		if i-1 >= 0:
			adj[i][j].append((i-1, j))
		if j-1 >= 0:
			adj[i][j].append((i, j-1))
		if i+1 < n:
			adj[i][j].append((i+1, j))
		if j+1 < m:
			adj[i][j].append((i, j+1))
	
visited = []
for i in xrange(n):
	visited.append([{} for j in xrange(m)])
	
ans = 0
threshold = n*m/2 
for i in xrange(n):
	for j in xrange(m):
		ans = max(ans, solve(i, j))
		if ans >= threshold:
			break
		
print ans