"""
Program to check if a graph is a path graph or not.
Input:
	T - # of test cases
	Then for each test case:
		V - # of vertices
		E - # of edges
		Then for each edge:
			u, v - indicating edge between u and v
Output:
	YES if it's a path graph.
	NO if it's not.
"""
HT = {}
visited = {}
flag = True

def addEdge(u, v):
	if u in HT:
		HT[u].append(v)
	else:
		HT[u] = [v]
	if v in HT:
		HT[v].append(u)
	else:
		HT[v] = [u]

def specDFS(v):
	visited[v] = 1
	if v != 1 and v != V:
		if v in HT and len(HT[v]) == 2 and v-1 in HT[v] and v+1 in HT[v]:
			flag = True
		else:
			flag = False
			return
	if v in HT:
		for node in HT[v]:
			if node not in visited:
				specDFS(node)
	else:
		flag = False
		return
		
for _ in range(input()):
	V = input()
	E = input()
	HT = {}
	visited = {}
	flag = True
	for e in range(E):
		u, v = map(int, raw_input().split())
		addEdge(u, v)
	specDFS(1)
	if flag == False:
		print "NO"
	else:
		for v in range(1, V+1):
			if v not in visited:
				print "NO"
				break
		else:
			print "YES"