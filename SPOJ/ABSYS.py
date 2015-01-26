import re
T = int(raw_input())
for t in range(T):
	bl = raw_input()
	s = raw_input()
	numbs = re.findall(r"[\w]+", s)
	if 'machula' in numbs[0]:
		print str(int(numbs[2])-int(numbs[1]))+" + "+numbs[1]+" = "+numbs[2]
	elif 'machula' in numbs[1]:
		print numbs[0]+" + "+str(int(numbs[2])-int(numbs[0]))+" = "+numbs[2]
	else:
		print numbs[0]+" + "+numbs[1]+" = "+str(int(numbs[0])+int(numbs[1]))
	