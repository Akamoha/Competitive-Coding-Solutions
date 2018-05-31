n, m = map(int, raw_input().split())
ans = n
for _ in xrange(m):
	l, r = map(int, raw_input().split())
	ans = min(ans, r-l+1)
print ans
for i in xrange(n):
	print i%ans,
print