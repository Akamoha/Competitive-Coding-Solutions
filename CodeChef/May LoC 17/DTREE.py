distances = {}
 
def DFS(s, d):
	global distances
	distances[s] = d
	for node in g[s]:
		if node not in distances:
			DFS(node, d+1)
 
def diameter(s):
	global distances
	distances = {}
	DFS(s, 0)
	maxi = distances.keys()[0]
	for i in distances:
		if distances[i] > distances[maxi]:
			maxi = i
 
	distances = {}
	DFS(maxi, 0)
	maxi = distances.keys()[0]
	for i in distances:
		if distances[i] > distances[maxi]:
			maxi = i
	return distances[maxi]
 
for _ in xrange(input()):
	N = input()
	g = [[] for _ in xrange(N+1)]
	for __ in xrange(N-1):
		u, v = map(int, raw_input().split())
		g[u].append(v)
		g[v].append(u)
 
	ds = []
	for i in xrange(1, N+1):
		newRoots = g[i]
		for node in newRoots:
			g[node].remove(i)
		dstemp = []
		for node in newRoots:
			dstemp.append(diameter(node))
		ds.append(max(dstemp))
		for node in newRoots:
			g[node].append(i)
 
	for d in ds:
		print d,
	print