n,a,b,c = map(int, raw_input().split())
rem = n%4
if rem == 0:
	print 0
elif rem == 1:
	print min(3*a, a+b, c)
elif rem == 2:
	print min(2*a, b, 2*c)
else:
	print min(a, b+c, 3*c)