while True:
	a, b = map(int, raw_input().split())
	if a == -1 and b == -1:
		break
	if a == 1 or b == 1:
		print str(a)+"+"+str(b)+"="+str(a+b)
	else:
		print str(a)+"+"+str(b)+"!="+str(a+b)