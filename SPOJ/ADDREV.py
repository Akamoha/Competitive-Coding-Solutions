N = int(raw_input())
for i in range(N):
	a,b = raw_input().split()
	s = str(int(a[::-1]) + int(b[::-1]))[::-1]
	i = 0
	while s[i] == '0':
		i += 1
	print s[i:]