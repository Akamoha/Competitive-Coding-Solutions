r=range
z=input
for _ in r(z()):
	A=[]
	D=[]
	n=z()
	for i in r(n):
		A.append(map(int,raw_input().split()))
		D+=[[0]*999]
	D[0]=[0]+A[0]+[0]
	for i in r(1,n):
		for j in r(1,i+2):
			D[i][j]=A[i][j-1]+max(D[i-1][j-1:j+1])
	print max(D[n-1])