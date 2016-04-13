for _ in xrange(input()):
	RGBvals,K=map(int,raw_input().split()),input()
	RGBvals.sort()
	X,Y,Z=RGBvals
	if K <= X:
		print 3*K-2
	elif K <= Y:
		print 2*K-1+X
	else:
		print Y+X+K