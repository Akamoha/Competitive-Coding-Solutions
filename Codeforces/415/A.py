n, m = map(int, raw_input().split())
m = map(int, raw_input().split())
for i in xrange(1, n+1):
	for button in m:
		if button <= i:
			print button,
			break
print