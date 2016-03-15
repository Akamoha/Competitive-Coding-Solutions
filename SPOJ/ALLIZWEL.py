str = "ALLIZZWELL"
visited = {}

def canBeVisited(node, l):
	global visited
	global str
	if l == len(str):
		return True
	if node in visited:
		return False
	if node[0] < 0 or node[0] >= R:
		return False
	if node[1] < 0 or node[1] >= C:
		return False
	if str[l] != M[node[0]][node[1]]:
		return False
	return True

def DFS(s, l):
	global visited
	global str
	if l == len(str):
		return True
	visited[s] = 1
	Nnode = (s[0]-1, s[1])
	Snode = (s[0]+1, s[1])
	Enode = (s[0], s[1]+1)
	Wnode = (s[0], s[1]-1)
	NEnode = (s[0]-1, s[1]+1)
	NWnode = (s[0]-1, s[1]-1)
	SEnode = (s[0]+1, s[1]+1)
	SWnode = (s[0]+1, s[1]-1)
	nodes = [Nnode, Snode, Enode, Wnode, NEnode, NWnode, SEnode, SWnode]
	for node in nodes:
		if canBeVisited(node, l+1):
			#print node, M[node[0]][node[1]]
			#print visited
			if DFS(node, l+1):
				return True
			visited.pop(node, None)
	return False

	
T = input()

R, C = map(int, raw_input().split())
M = []
Apositions = []
for r in xrange(R):
	M.append(raw_input())
for r in xrange(R):
	for c in xrange(C):
		if M[r][c] == 'A':
			Apositions.append((r,c))
for position in Apositions:
	visited = {}
	if DFS(position, 0):
		print "YES"
		break
else:
	print "NO"
	
for _ in range(T-1):
	lite = raw_input()
	R, C = map(int, raw_input().split())
	M = []
	Apositions = []
	for r in xrange(R):
		M.append(raw_input())
	for r in xrange(R):
		for c in xrange(C):
			if M[r][c] == 'A':
				Apositions.append((r,c))
	for position in Apositions:
		visited = {}
		if DFS(position, 0):
			print "YES"
			break
	else:
		print "NO"