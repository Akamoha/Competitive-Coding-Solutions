def compute(operand1, operand2, operator):
	x = int(operand1)
	y = int(operand2)
	if operator == '/':
		return x / y
	elif operator == '*':
		return x * y
	elif operator == '+':
		return x + y
	return x - y

def solve(eqn):
	if len(eqn) == 3:
		return compute(eqn[0], eqn[2], eqn[1])
	return compute(solve(eqn[:-2]), eqn[-1], eqn[-2])
	
for _ in range(input()):
	blankline = raw_input()
	eqn = raw_input().split()
	print solve(eqn[:-1])