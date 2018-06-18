M = 10**9+7
x, k = map(int, raw_input().split())
if k == 0:
	print (2*x)%M
elif x == 0:
	print 0
else:
	x %= M
	print ((4*x-2)%M*pow(2, k-1, M)+1)%M