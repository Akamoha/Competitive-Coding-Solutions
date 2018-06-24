import math

def check(k):
	global n
	candies, eaten = n, 0
	while candies > 0:
		eaten += min(k, candies)
		candies -= min(k, candies)
		candies -= candies/10
	return eaten >= int(math.ceil(n/2.0))

n = input()
lo, hi = 1, n
while lo < hi:
	mid = lo + (hi-lo)/2
	if check(mid):
		hi = mid
	else:
		lo = mid+1
print hi