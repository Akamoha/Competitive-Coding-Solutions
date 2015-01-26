import math
G, B = map(int, raw_input().split())
while G != -1 or B != -1:
	print int(math.ceil(1.0*max(G,B)/(min(G,B)+1)))
	G, B = map(int, raw_input().split())