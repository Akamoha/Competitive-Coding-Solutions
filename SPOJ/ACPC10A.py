while True:
	a1,a2,a3 = map(int, raw_input().split())
	if a1 == 0 and a2 == 0 and a3 == 0:
		break
	if (a2 - a1) == (a3 - a2):
		print "AP",
		print 2*a3 - a2
	else:
		print "GP",
		print a3 * a3 / a2