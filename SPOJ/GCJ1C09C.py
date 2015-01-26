import itertools

def costFinder(p, L):
	i = p
	while i < len(L):
		if L[i] != 0:
			i += 1
		else:
			break
	j = p-2
	while j >= 0:
		if L[j] != 0:
			j -= 1
		else:
			break
	return (i-j-2)
	

def getCost(P, perm):
	L = [1]*P
	cost = 0
	for p in perm:
		L[p-1] = 0
		cost += costFinder(p, L)
	return cost

N = int(raw_input())
for n in range(N):
	P, Q = map(int, raw_input().split())
	C = map(int, raw_input().split())
	if Q == 1:
		print "Case #"+str(n+1)+": "+str(P-1)
		continue
	perms = list(itertools.permutations(C))
	costs = []
	for perm in perms:
		costs.append(getCost(P, perm))
	print "Case #"+str(n+1)+": "+str(min(costs))