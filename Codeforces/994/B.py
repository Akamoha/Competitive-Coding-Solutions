def ii():
	return map(int, raw_input().split())
	
n, k = ii()
P = ii()
C = ii()

if k == 0:
	for c in C:
		print c,
	print
else:
	powers = [(p, i) for i, p in enumerate(P)]
	powers.sort()

	ans = [0 for _ in xrange(n)]
	
	lastk = []
	
	for j in xrange(1, n):
		if powers[j][0] > powers[j-1][0]:
			if len(lastk) < k:
				lastk.append(C[powers[j-1][1]])
			else:
				if min(lastk) < C[powers[j-1][1]]:
					lastk.pop(lastk.index(min(lastk)))
					lastk.append(C[powers[j-1][1]])
		ans[powers[j][1]] = sum(lastk)
	
	for i in xrange(n):
		print ans[i]+C[i],
	print
			