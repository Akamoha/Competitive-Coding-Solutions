"""
Partial! 30 pts.
"""
import sys
sys.setrecursionlimit(1000000)
from heapq import *
def addEdge(u, v, w):
	global HT
	global W
	if u not in HT:
		HT[u] = [v]
	else:
		HT[u].append(v)
	if v not in HT:
		HT[v] = [u]
	else:
		HT[v].append(u)
	W[(u, v)] = w
	W[(v, u)] = w
 
def getheights(s, p):
	global HT
	global W
	global heights
	global mxchild
	if s in HT:
		for node in HT[s]:
			if node != p:
				getheights(node, s)
	mx = 0
	mxnode = -1
	if s in HT:
		for node in HT[s]:
			if node != p:
				if heights[node] + W[(s, node)] >= mx:
					mx = heights[node] + W[(s, node)]
					mxnode = node
	#heights[s] = max([heights[node] + W[(s, node)] for node in HT[s] if node != p])
	heights[s] = mx
	mxchild[s] = mxnode
	
def getheights2(s, p):
	global HT
	global W
	global heights2
	global visited
	if s in HT:
		for node in HT[s]:
			if node != p:
				getheights2(node, s)
	try:
		heights2[s] = max([heights2[node] + W[(s, node)] for node in HT[s] if (node != p and node not in visited)])
	except:
		pass
 
def solve(s, p):
	global HT
	global heights
	global q
	if s in HT:
		for node in HT[s]:
			if node != p:
				q.append(heights[node] + W[(s, node)])
 
def solveDFS(s, p):
	global HT
	global q
	global heights
	global answer
	global mxchild
	global heights2
	q = []
	if s in HT:
		if len(HT[s]) == 1:
			answer[s] = 0
			return
	solve(s, p)
	mxq = max(q)
	cnt = 0
	for element in q:
		if element == mxq:
			cnt += 1
			if cnt > 1:
				break
	if cnt > 1:
		answer[s] = heights[s]
		visited[s] = 1
	else:
		temp1 = s
		temp2 = mxchild[temp1]
		while mxchild[temp2] != -1:
			temp1 = temp2
			temp2 = mxchild[temp1]
		heights2 = [0 for _ in xrange(temp)]
		getheights2(temp1, temp2)
		temp1 = s
		possibleanswers = []
		while temp1 != -1:
			temp2 = mxchild[temp1]
			lol = max(heights[temp1], heights2[temp1])
			if heights2[temp1] > heights[s]:
				break
			if lol != 0:
				possibleanswers.append(max(heights[temp1], heights2[temp1]))
			temp1 = temp2
		answer[s] = min(possibleanswers)
		visited[s] = 1
	
	for node in HT[s]:
		if node != p:
			solveDFS(node, s)
 
for _ in xrange(input()):
	N = input()
	HT = {}
	W = {}
	for _ in xrange(N-1):
		u, v, w = map(int, raw_input().split())
		addEdge(u, v, w)
	temp = N+1
	addEdge(1, temp, 0)
	temp += 1
	for node in xrange(2, N+1):
		if node in HT:
			if len(HT[node]) == 2:
				addEdge(node, temp, 0)
				temp += 1
	visited = {}
	heights2 = []
	heights = [0 for _ in xrange(temp)]
	mxchild = [0 for _ in xrange(temp)]
	getheights(1, 0)
	answer = [0 for _ in xrange(temp)]
	solveDFS(1, 0)
	for i in xrange(1, N+1):
		print answer[i] 