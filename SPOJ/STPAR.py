while(True):
	numCars = input()
	if numCars == 0:
		break
	cars = map(int, raw_input().split())
	needed = 1
	stack = []
	for i in range(numCars):
		if cars[i] == needed:
			needed += 1
			while len(stack) != 0 and stack[-1] == needed:
				stack.pop()
				needed += 1
		elif len(stack) != 0 and stack[-1] == needed:
			while len(stack) != 0 and stack[-1] == needed:
				stack.pop()
				needed += 1
		else:
			stack.append(cars[i])
	if len(stack) == 0:
		print "yes"
	else:
		print "no"