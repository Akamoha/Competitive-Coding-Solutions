A = map(int, raw_input().split())
ms = A[0]
s = 0
for i in range(0, len(A)):
	s += A[i]
	if s < 0:
		s = 0
	if s > ms:
		ms = s
print ms