x, y = map(int, raw_input().split())
if x == 1 and y == 1:
	print '='
elif x == 1:
	print '<'
elif y == 1:
	print '>'
elif x == 2 and y == 3:
	print '<'
elif x == 3 and y == 2:
	print '>'
elif x == y or (x == 2 and y == 4) or (x == 4 and y == 2):
	print '='
elif x < y:
	print '>'
else:
	print '<'