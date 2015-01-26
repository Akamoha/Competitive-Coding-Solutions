N, M = raw_input().split()
N = int(N)
M = int(M)
array = map(int, raw_input().split())
index = 0
for i in range(M):
	letter, number = raw_input().split()
	number = int(number)
	if letter == 'R':
		print array[(index-1+number) % N]
	elif letter == 'C':
		index += number
	elif letter == 'A':
		index -= number