def scalar_prod(A, B, C, D):
	return (B[0]-A[0])*(D[0]-C[0]) + (B[1]-A[1])*(D[1]-C[1])

def inside(v, sq):
	A, B, C, D, E = sq
	if 0 <= scalar_prod(A, v, A, B) <= scalar_prod(A, B, A, B) and 0 <= scalar_prod(A, v, A, D) <= scalar_prod(A, D, A, D):
		return True
	return False

def get_square():
	S = map(int, raw_input().split())
	return [(S[i], S[i+1]) for i in xrange(0, 7, 2)]

sq1, sq2 = get_square(), get_square()

sq1cx = (min([v[0] for v in sq1])+max([v[0] for v in sq1]))/2.0
sq1cy = (min([v[1] for v in sq1])+max([v[1] for v in sq1]))/2.0
sq2cx = (min([v[0] for v in sq2])+max([v[0] for v in sq2]))/2.0
sq2cy = (min([v[1] for v in sq2])+max([v[1] for v in sq2]))/2.0

sq1.append((sq1cx, sq1cy))
sq2.append((sq2cx, sq2cy))

for vertex in sq1:
	if inside(vertex, sq2):
		print "YES"
		break
else:
	for vertex in sq2:
		if inside(vertex, sq1):
			print "YES"
			break
	else:
		print "NO"