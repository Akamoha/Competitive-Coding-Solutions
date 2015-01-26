A, D = map(int, raw_input().split())
while A != 0 or D != 0:
	Batt = map(int, raw_input().split())
	Cdef = map(int, raw_input().split())
	Batt.sort()
	Cdef.sort()
	print "Y" if (Batt[0] < Cdef[1]) else "N"
	A, D = map(int, raw_input().split())