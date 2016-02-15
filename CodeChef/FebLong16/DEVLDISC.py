HT7 = {}
HT8 = {}

for x in range(7, 51, 3):
	HT7[x] = 1
	
for x in range(8, 51, 3):
	HT8[x] = 1

for _ in range(input()):
	n = input()
	if n <= 6:
		print -1
	elif n in HT7:
		print n
		print 1, 2
		print 1, 4
		print 2, 3
		print 3, 4
		for x in range(2, n-2):
			print x, x+3
		print 1
	elif n in HT8:
		print n
		print 1, 2
		print 1, 5
		print 2, 3
		print 4, 5
		print 3, 7
		print 4, 7
		print 2, 6
		print 5, 8
		for x in range(6, n-2):
			print x, x+3
		print 1
	else:
		print n+2
		print 1, 2
		print 1, 4
		print 2, 3
		print 3, 4
		print 2, 5
		print 3, 5
		print 4, 6
		print 3, 6
		print 4, 9
		print 2, 7
		print 3, 8
		for x in range(7, n-2):
			print x, x+3
		print 1