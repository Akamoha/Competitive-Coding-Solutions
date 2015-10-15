def solve(a, b):
	HTa = {}
	HTb = {}
	for letter in "abcdefghijklmnopqrstuvwxyz":
		HTa[letter] = HTb[letter] = 0
	for letter in a:
		HTa[letter] += 1
	for letter in b:
		HTb[letter] += 1
	ans = ""
	for letter in "abcdefghijklmnopqrstuvwxyz":
		if HTa[letter] == HTb[letter] or (HTa[letter] != 0 and HTb[letter] != 0):
			ans += letter*min(HTa[letter], HTb[letter])
	return ans

while True:
	try:
		a = raw_input()
		b = raw_input()
		print solve(a, b)
	except:
		break