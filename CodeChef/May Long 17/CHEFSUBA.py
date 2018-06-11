from collections import deque

N, K, P = map(int, raw_input().split())
if K > N:
	K = N
A = map(int, raw_input().split())
A = A+A
C = [0 for _ in xrange(2*N)]
C[K-1] = sum(A[:K])
cnt = C[K-1]
for i in xrange(K, 2*N):
	if A[i-K] == 0:
		cnt += A[i]
	else:
		cnt -= (1-A[i])
	C[i] = cnt
Q = raw_input()

C = C[K:]

k = N-K+1
Qi = deque()
for i in xrange(k):
	while Qi:
		if C[i] >= C[Qi[-1]]:
			Qi.pop()
		else:
			break
	Qi.append(i)

maxes = []
for i in xrange(k, len(C)):
	maxes.append(C[Qi[0]])
	while Qi and Qi[0] <= i-k:
		Qi.popleft()
	while Qi:
		if C[i] >= C[Qi[-1]]:
			Qi.pop()
		else:
			break
	Qi.append(i)
	
maxes.append(C[Qi[0]])

e = N-1
for q in Q:
	if q == '!':
		if e == 0:
			e = N-1
		else:
			e -= 1
	else:
		print maxes[e]