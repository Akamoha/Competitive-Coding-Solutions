N, M, H = map(int, raw_input().split())
NM = N*M
h = []
for _ in xrange(H):
	Tk, Ck = map(int, raw_input().split())
	h.append((Ck, Tk))
h.sort()
totalCellPainted = 0
cost = 0
for i in xrange(H):
	Ck, Tk = h[i]
	if totalCellPainted + Tk >= NM:
		cost += Ck*(NM - totalCellPainted)
		print cost
		break
	else:
		cost += Ck*Tk
		totalCellPainted += Tk
else:
	print "Impossible"