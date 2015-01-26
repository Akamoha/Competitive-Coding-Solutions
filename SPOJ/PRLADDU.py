T = int(raw_input())
for x in range(T):
	n = int(raw_input())
	D = map(int, raw_input().split())
	i = 0
	units = 0
	while i < len(D):
		if D[i] < 0:
			j = 0
			while D[i] < 0:
				if D[j] > 0:
					if D[j] > abs(D[i]):
						units += abs(j-i) * abs(D[i])
						D[j] += D[i]
						D[i] = 0
					else:
						units += abs(j-i) * D[j]
						D[i] += D[j]
						D[j] = 0
				j += 1
		i += 1
	print units