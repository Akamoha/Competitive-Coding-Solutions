def convertToJava(s):
	res = ""
	cap = False
	for l in s:
		if l == '_':
			cap = True
		elif cap:
			res += l.upper()
			cap = False
		else:
			res += l
	return res

def convertToCPP(s):
	res = ""
	for l in s:
		if l in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
			res += "_" + l.lower()
		else:
			res += l
	return res

while True:
	try:
		s = raw_input()
		if "_" in s:
			if "__" in s or s[-1] == "_" or s[0] == "_":
				print "Error!"
				continue
			for l in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
				if l in s:
					print "Error!"
					break
			else:
				print convertToJava(s)
		else:
			if s[0] not in "abcdefghijklmnopqrstuvwxyz":
				print "Error!"
			else:
				print convertToCPP(s)
	except:
		break