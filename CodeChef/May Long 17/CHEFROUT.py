def ispossible(log):
	i = 0
	while i < len(log) and log[i] == 'C':
		i += 1
	while i < len(log) and log[i] == 'E':
		i += 1
	while i < len(log) and log[i] == 'S':
		i += 1
	return "yes" if i == len(log) else "no"

for _ in xrange(input()):
	print ispossible(raw_input())