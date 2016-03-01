INFINITY = 10**9+7

V = input()
E = input()

HT = {}
W = {}
d = {}

def addDirEdge(u, v, w):
	if u in HT:
		HT[u].append(v)
	else:
		HT[u] = [v]
	W[(u, v)] = w

def relax(u, v):
	if d[v] > d[u] + W[(u, v)]:
		d[v] = d[u] + W[(u, v)]

def extractMin():
	global Q
	mnInd = 0
	mn = Q[0]
	for i in range(1, len(Q)):
		if d[mn] > d[Q[i]]:
			mnInd = i
			mn = Q[i]
	Q.pop(mnInd)
	return mn

for e in range(E):
	u, v, w = map(int, raw_input().split())
	addDirEdge(u, v, w)
	
source, dest = map(int, raw_input().split())
Q = range(1, V+1)

for v in Q:
	d[v] = INFINITY
d[source] = 0

while len(Q) != 0:
	u = extractMin()
	if u in HT:
		for v in HT[u]:
			relax(u, v)
		
print d[dest]