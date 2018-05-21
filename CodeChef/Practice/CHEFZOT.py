N = input()
A = map(int, raw_input().split())
count = 0
ans = 0
for a in A:
	if a != 0:
		count += 1
	else:
		count = 0
	ans = max(ans, count)
print ans