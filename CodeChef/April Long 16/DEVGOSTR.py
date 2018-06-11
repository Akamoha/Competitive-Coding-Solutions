"""
Partial! 60 pts.
"""
import itertools

def hammingdist(str1, str2):        
	diffs = 0
	for ch1, ch2 in zip(str1, str2):
		if ch1 != ch2:
			diffs += 1
	return diffs

def acceptable(s):
	for i in xrange(len(s)):
		for j in xrange(len(s)-1, i, -1):
			if (j-i) % 2 == 0:
				if s[i] == s[j] and s[i] == s[(i+j)/2]:
					return False
	return True
		
for _ in xrange(input()):
	A, K = map(int, raw_input().split())
	s = raw_input()
	if A == 1:
		print 1 if len(s) <= 2 else 0
	elif A == 2:
		if len(s) <= 8:
			c = 0
			for string in itertools.imap(''.join, itertools.product('ab', repeat=len(s))):
				if acceptable(string):
					if hammingdist(string, s) <= K:
						c += 1
			print c
		else:
			print 0
	else:
		if len(s) <= 30:
			c = 0
			for string in itertools.imap(''.join, itertools.product('abc', repeat=len(s))):
				if acceptable(string):
					if hammingdist(string, s) <= K:
						c += 1
			print c
		else:
			print 0