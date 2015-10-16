import math as m
while True:
	N = raw_input()
	if N == "00e0":
		break
	N = (10*int(N[0]) + int(N[1]))*(10**int(N[3]))
	power = pow(2, int(m.ceil(m.log(N)/m.log(2))))
	offset = power - N - 1
	print N - offset if offset != -1 else 1