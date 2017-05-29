from fractions import gcd
 
N, Q = map(int, raw_input().split())
A = map(int, raw_input().split())
gcds = {}
 
for i in xrange(N):
	for j in xrange(i, N):
		if i == j:
			previous = A[j]
		else:
			previous = gcd(previous, A[j])
		if previous not in gcds:
			gcds[previous] = 0
		if previous == 1:
			gcds[previous] += N-j
			break
		gcds[previous] += 1

sg = sorted(gcds)

for _ in xrange(Q):
	x = input()
	current = 0
	key = 0
	for key in sg:
		if current + gcds[key] < x:
			current += gcds[key]
		else:
			print key
			break
	else:
		print key