import math
import sys
sys.setrecursionlimit(1000000000)
F = [[1,1], [1,0]]
I = [[1,0], [0,1]]
negI = [[-1,0],[0,-1]]
MOD = 10**9+7

def matrixadd(X, Y):
	res = [[0,0],[0,0]]
	res[0][0] = (X[0][0]%MOD + Y[0][0]%MOD)%MOD
	res[0][1] = (X[0][1]%MOD + Y[0][1]%MOD)%MOD
	res[1][0] = (X[1][0]%MOD + Y[1][0]%MOD)%MOD
	res[1][1] = (X[1][1]%MOD + Y[1][1]%MOD)%MOD
	return res
	
def matrixmult(X, Y):
	res = [[0,0],[0,0]]
	res[0][0] = (((X[0][0]%MOD)*(Y[0][0]%MOD))%MOD + ((X[0][1]%MOD)*(Y[1][0]%MOD))%MOD)%MOD
	res[0][1] = (((X[0][0]%MOD)*(Y[0][1]%MOD))%MOD + ((X[0][1]%MOD)*(Y[1][1]%MOD))%MOD)%MOD
	res[1][0] = (((X[1][0]%MOD)*(Y[0][0]%MOD))%MOD + ((X[1][1]%MOD)*(Y[1][0]%MOD))%MOD)%MOD
	res[1][1] = (((X[1][0]%MOD)*(Y[0][1]%MOD))%MOD + ((X[1][1]%MOD)*(Y[1][1]%MOD))%MOD)%MOD
	return res

def matrixpow(X, N):
	if N == 1:
		return X
	if N%2 == 0:
		temp = matrixpow(X, N/2)
		return matrixmult(temp, temp)
	temp = matrixpow(X, N/2)
	temp = matrixmult(temp, temp)
	return matrixmult(X, temp)

def RMQhelper(qlow, qhigh, low, high, pos):
	if qlow <= low and qhigh >= high:
		return segTree[pos]
	if qlow > high or qhigh < low:
		return [[0,0],[0,0]]
	mid = (low+high)/2
	X, Y = RMQhelper(qlow, qhigh, low, mid, 2*pos+1), RMQhelper(qlow, qhigh, mid+1, high, 2*pos+2)
	return matrixadd(matrixadd(X, Y), matrixmult(X, Y))

def RMQ(qlow, qhigh):
	return RMQhelper(qlow, qhigh, 0, N-1, 0)

def constructTree(low, high, pos):
	if low == high:
		segTree[pos] = matrixpow(F, A[low])
	else:
		mid = (low+high)/2
		constructTree(low, mid, 2*pos+1)
		constructTree(mid+1, high, 2*pos+2)
		X, Y = segTree[2*pos+1], segTree[2*pos+2] 
		segTree[pos] = matrixadd(matrixmult(X,Y), matrixadd(X,Y))

def updateTree(low, high, pos, i, value):
	if low > i or high < i:
		return 
	if low == high:
		segTree[pos] = matrixpow(F, value)
	else:
		mid = (low+high)/2
		updateTree(low, mid, 2*pos+1, i, value)
		updateTree(mid+1, high, 2*pos+2, i, value)
		X, Y = segTree[2*pos+1], segTree[2*pos+2] 
		segTree[pos] = matrixadd(matrixmult(X,Y), matrixadd(X,Y))
		
N, M = map(int, raw_input().split())
A = map(int, raw_input().split())

segTree = [[[0,0],[0,0]] for _ in xrange(int(2**(math.ceil(math.log(N,2))+1))-1)]
constructTree(0, N-1, 0)

for _ in xrange(M):
	query = raw_input().split()
	i, j = int(query[1]), int(query[2])
	if query[0] == 'Q':
		print RMQ(i-1, j-1)[0][1]
	else:
		A[i-1] = j
		updateTree(0, N-1, 0, i-1, j)