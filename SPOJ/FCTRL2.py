t = int(raw_input())
for i in range(t):
	n = int(raw_input())
	fact = 1
	i = 2
	while i <= n:
		fact *= i
		i += 1
	print fact