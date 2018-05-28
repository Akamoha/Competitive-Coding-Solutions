import math

def solve(x):
	maxmoney = math.floor(x*abyb)
	low, high = 0, x
	while low < high:
		mid = (low+high)/2
		if mid*abyb < maxmoney:
			low = mid+1
		else:
			high = mid
	if mid*abyb >= maxmoney:
		return mid
	else:
		return mid+1

n, a, b = map(int, raw_input().split())
abyb = 1.0*a/b
X = map(int, raw_input().split())
for x in X:
	print x-solve(x),
print