for _ in xrange(input()):
	x, y = map(abs, map(int, raw_input().split()))
	ans = min(x, y)*2
	d = (max(x, y)-min(x, y))
	if x-min(x, y) == 0:
		d -= 1
		if y == x+1:
			ans += 1
		else:
			ans += 1
	if d%2 == 0:
		ans += d*2
	else:
		ans += (d+1)*2-1
	print ans