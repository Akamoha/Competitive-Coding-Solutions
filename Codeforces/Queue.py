n = input()
T = map(int, raw_input().split())
T.sort()
s = 0
ans = 0
for i in xrange(n):
	if s <= T[i]:
		ans += 1
		s += T[i]
print ans