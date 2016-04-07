for _ in xrange(input()):
	print "lxh" if sum([(raw_input()=="lxh") for _ in xrange(input())])%2!=0 else "hhb"