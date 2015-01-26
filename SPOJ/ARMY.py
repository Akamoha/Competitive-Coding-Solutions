T = int(raw_input())
for _ in range(T):
	blank = raw_input()
	NG, NM = map(int, raw_input().split())
	GodzillaArmy = map(int, raw_input().split())
	MechaGodzillaArmy = map(int, raw_input().split())
	if max(MechaGodzillaArmy) > max(GodzillaArmy):
		print "MechaGodzilla"
	else:
		print "Godzilla"