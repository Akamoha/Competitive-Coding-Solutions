T = int(raw_input())
for i in range(T):
	N = int(raw_input())
	count = 0
	for i in range(1,15):
		count += N/5**i
	print count