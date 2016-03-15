destination = 0
visited = {}

def canBeVisited(node):
	if node in visited:
		return False
	if node[0] < 0 or node[0] >= m:
		return False
	if node[1] < 0 or node[1] >= n:
		return False
	if M[node[0]][node[1]] == '#':
		return False
	return True

def specDFS(s):
	global destination
	visited[s] = 1
	if s == destination:
		return True
	upnode = (s[0]-1, s[1])
	downnode = (s[0]+1, s[1])
	leftnode = (s[0], s[1]-1)
	rightnode = (s[0], s[1]+1)
	if canBeVisited(upnode):
		if specDFS(upnode):
			return True
	if canBeVisited(downnode):
		if specDFS(downnode):
			return True
	if canBeVisited(leftnode):
		if specDFS(leftnode):
			return True
	if canBeVisited(rightnode):
		if specDFS(rightnode):
			return True
	return False
		

def thereIsAPathBetween(s, d):
	global destination
	global visited
	destination = d
	visited = {}
	return specDFS(s)
	
for _ in range(input()):
	m, n = map(int, raw_input().split())
	M = []
	for i in range(m):
		M.append(raw_input())
	openings = []
	for i in range(m):
		if M[i][0] == '.':
			openings.append((i,0))
		if n != 1 and M[i][n-1] == '.':
			openings.append((i,n-1))
	for j in range(1, n-1):
		if M[0][j] == '.':
			openings.append((0,j))
		if m != 1 and M[m-1][j] == '.':
			openings.append((m-1,j))
	if len(openings) != 2:
		print "invalid"
		continue
	source = openings[0]
	dest = openings[1]
	print "valid" if thereIsAPathBetween(source, dest) else "invalid"