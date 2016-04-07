import math
import sys
sys.setrecursionlimit(100000000)

INFINITY = 10**9+7

def RMQhelper(qlow, qhigh, low, high, pos):
	if qlow <= low and qhigh >= high:
		return segTree[pos]
	if qlow > high or qhigh < low:
		return INFINITY
	mid = (low+high)/2
	return min(RMQhelper(qlow, qhigh, low, mid, 2*pos+1), RMQhelper(qlow, qhigh, mid+1, high, 2*pos+2))

def RMQ(qlow, qhigh):
	return RMQhelper(qlow, qhigh, 0, N-1, 0)

def constructTree(low, high, pos):
	if low == high:
		segTree[pos] = A[low]
	else:
		mid = (low+high)/2
		constructTree(low, mid, 2*pos+1)
		constructTree(mid+1, high, 2*pos+2)
		segTree[pos] = min(segTree[2*pos+1], segTree[2*pos+2])
	
N = input()
A = map(int, raw_input().split())
segTree = [0 for _ in xrange(int(2**(math.ceil(math.log(N,2))+1))-1)]
constructTree(0, N-1, 0)

Q = input()
for q in xrange(Q):
	i, j = map(int, raw_input().split())
	print RMQ(i, j)