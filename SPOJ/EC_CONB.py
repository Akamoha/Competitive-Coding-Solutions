for _ in range(input()):
	n = input()
	print n if n%2 != 0 else int(bin(n)[2:][::-1], 2)