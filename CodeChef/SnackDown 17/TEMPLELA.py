for _ in xrange(input()):
	N = input()
	H = map(int, raw_input().split())
	if N%2 == 0:
		print "no"
		continue
	current = 1
	for h in H[:N/2+1]:
		if h != current:
			break
		current += 1
	else:
		current -= 1
		for h in H[N/2+1:]:
			current -= 1
			if h != current:
				break
		else:
			print "yes"
			continue
		print "no"
		continue
	print "no"
