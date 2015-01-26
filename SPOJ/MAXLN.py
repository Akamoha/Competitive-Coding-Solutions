T = int(raw_input())
for i in range(T):
	r = int(raw_input())
	s = 4*pow(r,2) + 0.25
	print "Case "+str(i+1)+": ",
	print("%.2f" % round(s,2))