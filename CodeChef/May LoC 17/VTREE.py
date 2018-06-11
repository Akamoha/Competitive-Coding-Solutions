def findNumTicks(s):
	visited[s] = 1
	numTicks[s] = int(s in ticked)
	for node in g[s]:
		if node not in visited:
			numTicks[s] += findNumTicks(node)
	return numTicks[s]

for _ in xrange(input()):
	n, l = map(int, raw_input().split())
	s = raw_input()
	char = {}
	parent = {}
	ticked = {}
	numTicks = [0 for _ in xrange(n+1)]
	g = [[] for _ in xrange(n+1)]
	for i in xrange(1, n+1):
		c, p = raw_input().split()
		p = int(p)
		char[i] = c
		parent[i] = p
		g[p].append(i)
	for i in xrange(1, n+1):
		t = i
		index = len(s)-1
		while char[t] == s[index]:
			if index == 0:
				ticked[i] = 1
				break
			index -= 1
			t = parent[t]
			if t == 0:
				break
	visited = {}
	findNumTicks(1)
	for ans in numTicks[1:]:
		print ans,
	print