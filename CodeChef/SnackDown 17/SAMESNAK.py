for _ in xrange(input()):
	X1, Y1, X2, Y2 = map(int, raw_input().split())
	X3, Y3, X4, Y4 = map(int, raw_input().split())
	if (X1, Y1) in [(X3, Y3), (X4, Y4)]:
		print "yes"
		continue
	if (X2, Y2) in [(X3, Y3), (X4, Y4)]:
		print "yes"
		continue
	if X1 == X2 and X2 == X3 and X3 == X4:
		smallY = min(Y1, Y2, Y3, Y4)
		if smallY == Y1:
			if min(Y3, Y4) <= Y2:
				print "yes"
				continue
		if smallY == Y2:
			if min(Y3, Y4) <= Y1:
				print "yes"
				continue
		if smallY == Y3:
			if min(Y1, Y2) <= Y4:
				print "yes"
				continue
		if smallY == Y4:
			if min(Y1, Y2) <= Y3:
				print "yes"
				continue
	if Y1 == Y2 and Y2 == Y3 and Y3 == Y4:
		smallX = min(X1, X2, X3, X4)
		if smallX == X1:
			if min(X3, X4) <= X2:
				print "yes"
				continue
		if smallX == X2:
			if min(X3, X4) <= X1:
				print "yes"
				continue
		if smallX == X3:
			if min(X1, X2) <= X4:
				print "yes"
				continue
		if smallX == X4:
			if min(X1, X2) <= X3:
				print "yes"
				continue
	print "no"