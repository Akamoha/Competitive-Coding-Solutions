n = input()
A = map(int, raw_input().split())
ht = {}
for a in A:
	if a != 0:
		ht[a] = 1
print len(ht)