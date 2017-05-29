def solve(i, condition):
	global started
	if i == n:
		return True
	""" . """
	""" . """
	if row1[i] == '.' and row2[i] == '.':
		if started:
			return('#' not in row1[i:] and '#' not in row2[i:])
		return solve(i+1, condition)

	""" # """
	""" . """
	if row1[i] == '#' and row2[i] == '.':
		started = True
		if condition == "anything":
			return solve(i+1, "top")
		if condition == "top":
			return solve(i+1, "top")
		if condition == "bottom":
			return False

	""" . """
	""" # """
	if row1[i] == '.' and row2[i] == '#':
		started = True
		if condition == "anything":
			return solve(i+1, "bottom")
		if condition == "top":
			return False
		if condition == "bottom":
			return solve(i+1, "bottom")

	""" # """
	""" # """
	if row1[i] == '#' and row2[i] == '#':
		started = True
		if condition == "anything":
			return solve(i+1, "anything")
		if condition == "top":
			return solve(i+1, "bottom")
		if condition == "bottom":
			return solve(i+1, "top")

for _ in xrange(input()):
	n = input()
	row1 = raw_input()
	row2 = raw_input()
	started = False
	print "yes" if solve(0, "anything") else "no"