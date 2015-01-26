while True:
	N = int(raw_input())
	if N == -1:
		break
	else:
		candies = []
		count = 0
		for i in range(N):
			x = int(raw_input())
			candies.append(x)
			count += x
		if count % N != 0:
			print "-1"
		else:
			diff = 0
			mean = count/N
			for candy in candies:
				diff += abs(candy - mean)
			print diff/2
			