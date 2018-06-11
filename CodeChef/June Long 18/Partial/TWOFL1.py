import sys
sys.setrecursionlimit(2147000000)

def inp():
	return map(int, raw_input().split())

def DFS(i, j, a, b):
	size = 0
	visited[(i, j)] = 1
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
		if A[x][y] in [a, b] and (x, y) not in visited:
			size += DFS(x, y, a, b)
	return 1+size
	
def solve(a, b):
	size = 0
	for i in xrange(n):
		for j in xrange(m):
			if A[i][j] in [a, b] and (i, j) not in visited:
				size = max(size, DFS(i, j, a, b))
	return size

n, m = inp()
A = []
for _ in xrange(n):
	A.append(inp())

sizes = []
for i in xrange(1, 101):
	for j in xrange(i, 101):
		visited = {}
		sizes.append(solve(i, j))
		
print max(sizes)