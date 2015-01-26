import math
N = int(raw_input())
i = 2
count = N
s = math.sqrt(N)
while i <= s:
	j = i
	while (j * i) <= N:
		count += 1
		j += 1
	i += 1
print count