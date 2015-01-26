t = int(raw_input())
for i in range(t):
	N = int(raw_input())
	MenHotness = map(int, raw_input().split())
	WomenHotness = map(int, raw_input().split())
	MenHotness.sort()
	WomenHotness.sort()
	j = 0
	bondSum = 0
	while j < N:
		bondSum += MenHotness[j]*WomenHotness[j]
		j += 1
	print bondSum