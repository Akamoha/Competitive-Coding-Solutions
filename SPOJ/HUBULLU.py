t = int(raw_input())
for _ in range(t):
	N, start = map(int, raw_input().split())
	print "Airborne wins." if start == 0 else "Pagfloyd wins."