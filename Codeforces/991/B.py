n = input()
A = map(int, raw_input().split())
s = sum(A)
if s*10.0/n >= 45:
	print 0
else:
	ans = 0
	A.sort()
	for a in A:
		ans += 1
		s = s-a+5
		if s*10.0/n >= 45:
			break
	print ans