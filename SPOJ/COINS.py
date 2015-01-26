def split(n):
	if n/4 + n/3 + n/2 < n:
		return n
	else:
		return split(n/4) + split(n/3) + split(n/2)

while 1:
	try:
		n = int(raw_input())
		print split(n)
	except:
		break