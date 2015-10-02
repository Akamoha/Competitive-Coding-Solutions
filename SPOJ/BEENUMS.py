def is_square(apositiveint):
  x = apositiveint // 2
  seen = set([x])
  while x * x != apositiveint:
    x = (x + (apositiveint // x)) // 2
    if x in seen: return 'N'
    seen.add(x)
  return 'Y'

while True:
	N = input()
	if N == -1:
		break
	if N == 1:
		print 'Y'
		continue
	print is_square(int((4*N - 1)/3))