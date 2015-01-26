a = [0]
isThere = {}
isThere[0] = 1
for i in range(1,500001):
	if (a[i-1] - i) > 0 and (a[i-1] - i) not in isThere:
		a.append(a[i-1] - i)
		isThere[a[i-1] - i] = 1
	else:
		a.append(a[i-1] + i)
		isThere[a[i-1] + i] = 1
		
k = int(raw_input())
while k != -1:
	print a[k]
	k = int(raw_input())