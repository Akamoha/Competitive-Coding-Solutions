import math

CSA = [0]

for i in xrange(1, 25001):
	CSA.append(CSA[-1] + math.log(i)/math.log(10))

for _ in xrange(input()):
	N = input()
	A = map(int, raw_input().split())
	for a in A:
		print int(math.floor(CSA[a]))+1,
	print

# The solution below works too lol

"""
factorial = [1]

ans = 1
for i in xrange(1, 25001):
	ans *= i
	factorial.append(ans)

for _ in xrange(input()):
	N = input()
	A = map(int, raw_input().split())
	for a in A:
		print len(str(factorial[a])),
	print
"""