import sys
sys.setrecursionlimit(2147483647)

def adjList(node):
	x, y = node
	return [(x+1,y), (x,y+1), (x-1,y), (x,y-1)]

def canBeVisited(node):
	x, y = node
	if x < 0 or y < 0 or x >= R or y >= C or maze[x][y] == '#': 
		return False
	return True

def DFS(s, depth):
	try:
		depths[s] = depth
		for node in adjList(s):
			if node not in depths and canBeVisited(node):
				DFS(node, depth+1)
	except:
		pass

for _ in xrange(input()):
	try:
		C, R = map(int, raw_input().split())
		maze = []
		depths = {}
		for _ in xrange(R):
			maze.append(list(raw_input()))
		row, col = 0, 0
		for r in xrange(R):
			for c in xrange(C):
				if maze[r][c] == '.':
					row, col = r, c
					break
		r, c = row, col
		DFS((r, c), 0)
		maxdepthnode = -1
		maxdepth = -1
		for i in depths:
			if maxdepth < depths[i]:
				maxdepthnode = i
				maxdepth = depths[i]
		depths = {}
		DFS(maxdepthnode, 0)
		maxdepth = -1
		for i in depths:
			if maxdepth < depths[i]:
				maxdepth = depths[i]
		print "Maximum rope length is "+str(maxdepth)+"."
	except:
		pass