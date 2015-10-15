import math as m
for _ in range(input()):
	a, b, c, d = map(float, raw_input().split())
	s = (a + b + c + d)/2
	print "{:.2f}".format(m.sqrt((s-a)*(s-b)*(s-c)*(s-d)))