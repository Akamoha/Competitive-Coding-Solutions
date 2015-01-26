T = int(raw_input())
for t in range(T):
	n = int(raw_input())
	i = 1
	while n > (i*(i+1)/2):
		i += 1
	numerator = i - ((i*(i+1)/2) - n)
	denominator = i + 1 - numerator
	print ("TERM "+str(n)+" IS "+str(numerator)+"/"+str(denominator)) if (i % 2 == 1) else ("TERM "+str(n)+" IS "+str(denominator)+"/"+str(numerator))