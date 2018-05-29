import random

def permute(x):
	global N
	if x == "Petr":
		swaps = 3*N
	else:
		swaps = 7*N+1
	for _ in xrange(swaps):
		i = random.randint(0, N-1)
		j = random.randint(0, N-1)
		while j == i:
			j = random.randint(0, N-1)
		A[i], A[j] = A[j], A[i]

def solve():
	c = 0
	position = {}
	for i in xrange(N):
		position[A[i]] = i
	for i in xrange(N):
		if position[i+1] != i:
			num = A[i]
			A[position[i+1]], A[i] = A[i], A[position[i+1]]
			position[num] = position[i+1]
			position[i+1] = i
			c += 1
	print c
	if N%2 == 0:
		if c%2 == 0:
			return "Petr"
		else:
			return "Um_nik"
	else:
		if c%2 == 0:
			return "Um_nik"
		else:
			return "Petr"

N = input()
for i in xrange(1):
	A = range(1, N+1)
	permute("Petr")
	if solve() != "Petr":
		print "WA"
		break
	A = range(1, N+1)
	permute("Um_nik")
	if solve() != "Um_nik":
		print "WA"
		break
else:
	print "AC"