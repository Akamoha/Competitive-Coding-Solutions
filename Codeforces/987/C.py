INF = 10**9+7
n = input()
s = map(int, raw_input().split())
c = map(int, raw_input().split())
DP1 = [cost for cost in c]
DP2 = [INF for _ in xrange(n)]
DP3 = [INF for _ in xrange(n)]
for i in xrange(1, n):
	for j in xrange(i):
		if s[j] < s[i]:
			DP2[i] = min(DP2[i], DP1[j]+c[i])
for i in xrange(2, n):
	for j in xrange(1, i):
		if s[j] < s[i]:
			DP3[i] = min(DP3[i], DP2[j]+c[i])
ans = min(DP3)
print ans if ans != INF else -1