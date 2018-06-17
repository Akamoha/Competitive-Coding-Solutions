def ii():
	return map(int, raw_input().split())
	
n, m = ii()
X = ii()
Y = ii()

ht = {}
for y in Y:
	ht[y] = 1

for x in X:
	if x in ht:
		print x,
print