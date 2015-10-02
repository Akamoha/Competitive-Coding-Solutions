import math as m

def rec(N):
	s = '{0:020b}'.format(N)
	ans = ""
	if N == 1:
		return "2(0)"
	elif N == 2:
		return "2"
	elif N == 4:
		return "2(2)"
	if s.count('1') == 1:
		return "2("+str(rec(19 - s.index('1')))+")"
	for i in range(20):
		if s[i] == '1':
			ans += rec(2**(19-i)) + "+"
	return ans[0:-1]
	
while True:
	N = input()
	print str(N)+"="+rec(N)