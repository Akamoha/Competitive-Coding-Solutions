N = int(raw_input())
A = []
B = []
C = []
hashtable = {}
for _ in range(N):
	a, b, c = map(int, raw_input().split())
	A.append(a)
	B.append(b)
	C.append(c)
	if c not in hashtable:
		hashtable[c] = len(C)-1
	
results = []
for i in range(len(A)):
	for j in range(len(B)):
		if (A[i]+B[j]) in hashtable:
			results.append(str(i)+" "+str(j)+" "+str(hashtable[(A[i]+B[j])]))
			
print len(results)
for x in results:
	print x

