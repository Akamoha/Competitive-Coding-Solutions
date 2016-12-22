n = input()
HT = {}
for letter in "abcdefghijklmnopqrstuvwxyz ":
	HT[letter] = letter
code = raw_input()
for i in xrange(n):
	HT[code[i]] = code[(i+1)%n]
for _ in xrange(input()):
	plaintext = raw_input()
	ans = ""
	for letter in plaintext:
		ans+=HT[letter]
	print ans