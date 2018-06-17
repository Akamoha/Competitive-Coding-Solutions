from collections import deque

class edge:
	def __init__(self, u, v, cap):
		self.u = u
		self.v = v
		self.cap = cap

class flow_network:
	def __init__(self, n):
		self.n = n
		self.edges = [[] for _ in xrange(n+1)]
	
	def add_edge(self, u, v, cap):
		e = edge(u, v, cap)
		rev = edge(v, u, 0)
		e.rev = rev
		rev.rev = e
		self.edges[u].append(e)
		self.edges[v].append(rev)
		
	def augment(self, s, t):
		visited = {}
		q = deque()
		q.append(s)
		visited[s] = edge(0, 0, 0)
		while q:
			u = q.pop()
			for i in xrange(len(self.edges[u])):
				v = self.edges[u][i].v
				if v not in visited and self.edges[u][i].cap > 0:
					visited[v] = self.edges[u][i]
					q.append(v)
		
		if t not in visited:
			return 0
		
		stack = []
		stack.append(visited[t])
		bneck = visited[t].cap
		while stack[-1].u != s:
			stack.append(visited[stack[-1].u])
			bneck = min(bneck, stack[-1].cap)
		
		while stack:
			stack[-1].cap -= bneck
			stack[-1].rev.cap += bneck
			stack.pop()
			
		return bneck

	def max_flow(self, source, sink):
		flow = 0
		while True:
			f = self.augment(source, sink)
			if f == 0:
				break
			flow += f
		return flow

N, M, W, K, R = map(int, raw_input().split())

wallH = [[0 for i in xrange(M+2)] for j in xrange(N+2)]
wallV = [[0 for i in xrange(M+2)] for j in xrange(N+2)]

for _ in xrange(W):
	X1, Y1, X2, Y2 = map(int, raw_input().split())
	if X2 > X1:
		wallV[X2][Y2] = 1
	elif X2 < X1:
		wallV[X1][Y1] = 1
	elif Y2 > Y1:
		wallH[X1][Y1] = 1
	else:
		wallH[X2][Y2] = 1
		
G = flow_network(R+2)

room = [[0 for i in xrange(M+2)] for j in xrange(N+2)]

for r in xrange(1, R+1):
	X, Y, C1, C2 = map(int, raw_input().split())
	G.add_edge(0, r, C1)
	G.add_edge(r, R+1, C2)
	q = [(X, Y)]
	while q:
		i, j = q.pop()
		if i < 1 or j < 1 or i > N or j > M:
			continue
		if room[i][j] != 0:
			continue
		room[i][j] = r
		if wallH[i][j] != 1:
			q.append((i, j+1))
		if wallH[i][j-1] != 1:
			q.append((i, j-1))
		if wallV[i][j] != 1:
			q.append((i-1, j))
		if wallV[i+1][j] != 1:
			q.append((i+1, j))

costs = [[0 for i in xrange(R+1)] for j in xrange(R+1)]

for i in xrange(1, N+1):
	for j in xrange(1, M+1):
		if wallH[i][j]:
			mn = min(room[i][j], room[i][j+1])
			mx = max(room[i][j], room[i][j+1])
			costs[mn][mx] += K
		if wallV[i][j]:
			mn = min(room[i-1][j], room[i][j])
			mx = max(room[i-1][j], room[i][j])
			costs[mn][mx] += K

for i in xrange(1, R+1):
	for j in xrange(i+1, R+1):	
		if costs[i][j]:
			G.add_edge(i, j, costs[i][j])
			G.add_edge(j, i, costs[i][j])

print G.max_flow(0, R+1)