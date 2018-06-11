N = input()
dict = {}
for i in xrange(1, N+1):
	S = raw_input()
	d = dict
	for c in S[:-1]:
		if c not in d:
			d[c] = [{}, i, []]
		d = d[c][0]
	c = S[-1]
	if c not in d:
		d[c] = [{}, i, [i]]
	else:
		d[c][2].append(i)
Q = input()
for _ in xrange(Q):
	R, P = raw_input().split()
	R = int(R)
	d = dict
	ans = ""
	final = False
	flag = False
	fi = False
	for c in P[:-1]:
		if c in d and d[c][1] <= R:
			ans += c
			fi = len(d[c][2]) != 0 and min(d[c][2]) <= R
			d = d[c][0]
		else:
			flag = True
			break
	if flag == False:
		c = P[-1]
		if c in d and d[c][1] <= R:
			ans += c
			fi = len(d[c][2]) != 0 and min(d[c][2]) <= R
			if fi:
				final = True
			else:
				d = d[c][0]
		else:
			flag = True
	if flag and fi:
		final = True
	while not final:
		if d == {}:
			break
		for key in sorted(d):
			if d[key][1] <= R:
				break
		else:
			break
		ans += key
		if len(d[key][2]) != 0 and min(d[key][2]) <= R:
			break
		d = d[key][0]
	print ans