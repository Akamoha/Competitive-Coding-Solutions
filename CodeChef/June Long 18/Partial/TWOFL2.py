import sys
sys.setrecursionlimit(2147000000)

def inp():
	return map(int, raw_input().split())

def DFS(i, j, a, b):
	size = 0
	mn, mx = min(a, b), max(a, b)
	visited[i][j][(mn, mx)] = 1
	adj = []
	if i-1 >= 0:
		adj.append((i-1, j))
	if j-1 >= 0:
		adj.append((i, j-1))
	if i+1 < n:
		adj.append((i+1, j))
	if j+1 < m:
		adj.append((i, j+1))
	for x, y in adj:
		if (mn, mx) not in visited[x][y]:
			if A[x][y] in [a, b]:
				size += DFS(x, y, a, b)
	return 1+size
	
def solve(i, j):
	size = 0
	adj = []
	if i-1 >= 0:
		adj.append((i-1, j))
	if j-1 >= 0:
		adj.append((i, j-1))
	if i+1 < n:
		adj.append((i+1, j))
	if j+1 < m:
		adj.append((i, j+1))
	flowers = {}
	for x, y in adj:
		flowers[A[x][y]] = 1
	for f in flowers:
		mn, mx = min(A[i][j], f), max(A[i][j], f)
		if (mn, mx) not in visited[i][j]:
			size = max(size, DFS(i, j, A[i][j], f))
	return size

n, m = inp()
A = []
for _ in xrange(n):
	A.append(inp())

	
visited = []
for i in xrange(n):
	visited.append([{} for j in xrange(m)])
	
ans = 0
for i in xrange(n):
	for j in xrange(m):
		ans = max(ans, solve(i, j))
		
print ans	