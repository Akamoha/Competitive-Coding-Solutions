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

idx = {}
i = 0
for l in "abcdefghijklmnopqrstuvwxyz":
	idx[l] = i
	i += 1
for l in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
	idx[l] = i
	i += 1

G = flow_network(52)

for i in xrange(input()):
	A, B, F = raw_input().split()
	G.add_edge(idx[A], idx[B], int(F))

print G.max_flow(idx['A'], idx['Z'])