reversealphabet = "abcdefghijklmnopqrstuvwxyz"[::-1]
s = raw_input()
letters = []
for i in xrange(len(s)):
	letters.append((s[i], i))
HT = {}
for letter in reversealphabet:
	HT[letter] = []
for i in xrange(len(s)):
	HT[letters[i][0]].append(letters[i][1])
index = -1
answer = ""
for letter in reversealphabet:
	for ind in HT[letter]:
		if ind > index:
			answer += letter
			index = ind
print answer