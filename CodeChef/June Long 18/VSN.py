EPSILON = 10**-2
	
def check(t):
	Ax = Qx + dx*t - Px
	Ay = Qy + dy*t - Py
	Az = Qz + dz*t - Pz
	
	a = sum([A**2 for A in [Ax, Ay, Az]])
	b = 2*(Ax*(Px-cx) + Ay*(Py-cy) + Az*(Pz-cz))
 
	delta = b**2 - 4*a*c
	if abs(delta) <= EPSILON:
		return 1
	elif delta > 0:
		return 2
	return 0
	
for _ in xrange(input()):
	Px, Py, Pz, Qx, Qy, Qz, dx, dy, dz, cx, cy, cz, r = map(int, raw_input().split())
	
	c = sum([cP**2 for cP in [cx, cy, cz, Px, Py, Pz]]) - r**2 - 2*(Px*cx + Py*cy + Pz*cz)
	
	low = 0
	high = 10**9+1
	while low < high-10**-6:
		mid = low + (high-low)*1.0/2
		intersections = check(mid)
		if intersections == 1:
			break
		elif intersections > 1:
			low = mid
		else:
			high = mid
	print mid 