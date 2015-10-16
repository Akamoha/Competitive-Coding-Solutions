import math
HT = {"1/4": 0, "1/2": 0, "3/4": 0}
for _ in range(input()):
	n = raw_input()
	HT[n] += 1
count = 0
m = min(HT["3/4"], HT["1/4"])
HT["3/4"] -= m
HT["1/4"] -= m
count += m
if HT["3/4"] > 0:
	count += HT["3/4"]
	count += int(math.ceil(HT["1/2"]/2.0))
	print count + 1
elif HT["1/4"] > 0:
	count += HT["1/4"]/4
	HT["1/4"] = HT["1/4"]%4
	if HT["1/4"] == 0:
		count += int(math.ceil(HT["1/2"]/2.0))
		print count + 1
	elif HT["1/4"] == 1 or HT["1/4"] == 2:
		count += HT["1/2"]/2
		print count + 2
	else:
		count += int(math.ceil(HT["1/2"]/2.0))
		print count + 2
else:
	count += int(math.ceil(HT["1/2"]/2.0))
	print count + 1