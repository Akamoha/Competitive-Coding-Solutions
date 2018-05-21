n = input()
s = raw_input()
if n == 1:
	if s[0] == '1':
		print "Yes"
	else:
		print "No"
else:
	for i in xrange(1, n-1):
		if s[i] == '1':
			if s[i-1] == '1' or s[i+1] == '1':
				print "No"
				break
		else:
			if s[i-1] == '0' and s[i+1] == '0':
				print "No"
				break
	else:
		if s[0] != s[1] and s[-1] != s[-2]:
			print "Yes"
		else:
			print "No"