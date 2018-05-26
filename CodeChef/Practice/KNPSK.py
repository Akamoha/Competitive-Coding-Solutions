N = input()
M = 0
costW1 = []
costW2 = []
for _ in xrange(N):
	W, C = map(int, raw_input().split())
	M += W
	if W == 1:
		costW1.append(C)
	else:
		costW2.append(C)
	
costW1.sort()
costW2.sort()
n1 = len(costW1)-1
n2 = len(costW2)-1

ans = [0 for _ in xrange(M+1)]

for C in xrange(2, M+1, 2):
	pos1, pos2 = 0, 0
	if n1 == 0:
		pos1 = costW1[n1]
	elif n1 > 0:
		pos1 = costW1[n1] + costW1[n1-1]
	if n2 >= 0:
		pos2 = costW2[n2]
	if pos1 > pos2:
		ans[C] = ans[C-2] + pos1
		n1 -= 2
	else:
		ans[C] = ans[C-2] + pos2
		n2 -= 1

n1 = len(costW1)-1
n2 = len(costW2)-1

if n1 >= 0:
	ans[1] = costW1[n1]
	n1 -= 1

for C in xrange(3, M+1, 2):
	pos1, pos2 = 0, 0
	if n1 == 0:
		pos1 = costW1[n1]
	elif n1 > 0:
		pos1 = costW1[n1] + costW1[n1-1]
	if n2 >= 0:
		pos2 = costW2[n2]
	if pos1 > pos2:
		ans[C] = ans[C-2] + pos1
		n1 -= 2
	else:
		ans[C] = ans[C-2] + pos2
		n2 -= 1
		
for a in ans[1:]:
	print a,
print
		
		