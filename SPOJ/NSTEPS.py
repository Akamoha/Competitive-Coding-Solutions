N = int(raw_input())
for i in range(N):
	x,y = map(int, raw_input().split())
	if x == y:
		number = (x * 2) if (x % 2 == 0) else (x * 2 - 1)
	elif x == y + 2:
		number = (x + y) if (x % 2 == 0) else (x + y - 1)
	else:
		number = "No Number"
	print number