while True:
	c = float(raw_input())
	if c == 0.00:
		break
	else:
		totalOverhang = 0.00
		den = 2.00
		while totalOverhang < c:
			totalOverhang += 1.00/den
			den += 1.00
		print str(int(den-2))+" card(s)"