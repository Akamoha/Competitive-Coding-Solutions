flips = 0
for b in raw_input()[::-1]:
	flips += int(flips%2==1-int(b))
print flips