def convert(stringToConvert):
	return stringToConvert[2]+stringToConvert[0]+stringToConvert[1]

t = int(raw_input())
for _ in range(t):
	s = raw_input()
	l = []
	for i in range(len(s)):
		if s[i] != ')':
			l.append(s[i])
		else:
			temp = []
			while l[-1] != '(':
				temp.append(l.pop(-1))
			l.pop(-1)
			l.append(convert(temp))
			
	print l[0]
			