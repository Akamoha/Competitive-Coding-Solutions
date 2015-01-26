N, M = map(int, raw_input().split())
A = list(raw_input())

x = []

def computex():
	sum = 0
	for i in range(N):
		sum = (sum + int(A[i]))
		x.append(sum)
	
computex()
for m in range(M):
	type, P, Q = raw_input().split()
	if type == '2':
		y = x
		if int(P)-2 >= 0:
			for i in range(int(P)-1,int(Q)):
				y[i] -= y[int(P)-2]
				y[i] %= 3
		else:
			for i in range(int(P)-1,int(Q)):
				y[i] %= 3
		B = [0]*3
		B[0] = y[int(P)-1:int(Q)].count(0) + 1
		B[1] = y[int(P)-1:int(Q)].count(1)
		B[2] = y[int(P)-1:int(Q)].count(2)
		ans = 0
		for i in range(3):
			ans += B[i]*(B[i]-1)/2
		print ans
	elif type == '1':
		A[int(P)-1] = Q
		x = []
		computex()