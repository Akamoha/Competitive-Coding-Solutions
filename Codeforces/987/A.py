n = input()
seen = {}
for i in xrange(n):
	seen[raw_input()] = 1
c2N = {}
c2N["purple"] = "Power"
c2N["green"] = "Time"
c2N["blue"] = "Space"
c2N["orange"] = "Soul"
c2N["red"] = "Reality"
c2N["yellow"] = "Mind"

ans = 0
colors = []
for i in c2N:
	if i not in seen:
		ans += 1
		colors.append(c2N[i])
print ans
for c in colors:
	print c