import math
def fun(X,b,k):
	i = 0
	m = 1
	while i < b:
		m = X*m
		m = int(str(m)[:int(math.ceil(k+((math.log(b)/math.log(10)))))])
		i += 1
	return m


T = int(raw_input())
for t in range(T):	
	X, Y = raw_input().split()
	X = int(X)
	b = 1
	while True:
		if str(fun(X,b,len(Y)))[:len(Y)] == Y:
			print "Case "+str(t+1)+": "+str(b)
			break
		b += 1