def countiscloser(count, othernum):
	return abs(count - 100) < abs(othernum - 100)

count = 0
for _ in range(10):
	n = input()
	if countiscloser(count, count + n):
		print count
		break
	else:
		count += n
else:
	print count