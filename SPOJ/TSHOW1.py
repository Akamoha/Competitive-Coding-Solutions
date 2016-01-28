import math
for _ in range(input()):
	k = input()
	l = int(math.log(k+1)/math.log(2))
	fs = '{0:0'+str(l)+'b}'
	ans = fs.format(k-2**l+1)
	ans = ans.replace('0', '5')
	print ans.replace('1', '6')