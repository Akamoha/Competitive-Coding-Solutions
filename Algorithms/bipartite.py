"""
Program to check if a connected graph is bipartite or not.
Input:
	V - # of vertices
	E - # of edges
	Then for each edge:
		u, v - indicating edge between u and v
Output:
	YES if it's a bipartite graph.
	NO if it's not.
"""
V = input()
E = input()
HT = {}

def addEdge(u, v):
	if u in HT:
		HT[u].append(v)
	else:
		HT[u] = [v]
	if v in HT:
		HT[v].append(u)
	else:
		HT[v] = [u]

sets = [{}, {}]
visited = {}

def DFS(v, sn):
	global flag
	for node in HT[v]:
		if node in sets[sn]:
			flag = False
			return
		sets[1-sn][node] = 1
	for node in HT[v]:
		if node not in visited:
			visited[node] = 1
			DFS(node, 1-sn)
	
for e in range(E):
	u, v = map(int, raw_input().split())
	addEdge(u, v)

flag = True
visited[1] = 1
sets[0][1] = 1
DFS(1, 0)
if flag == False:
	print "NO"
else:
	print "YES"
print sets[0].keys()
print sets[1].keys()