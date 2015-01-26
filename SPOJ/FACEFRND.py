N = int(raw_input())
friends = []
ID = {}
for i in range(N):
	F = map(int, raw_input().split())
	ID[F.pop(0)] = 1
	F.pop(0)
	for f in F:
		friends.append(f)
	
count = 0
for f in list(set(friends)):
	if f in ID:
		continue
	else:
		count += 1

print count