A, B, C, N = map(int, raw_input().split())
passed = A+B-C
if C > A or C > B or passed < 0 or passed > N-1:
	print -1
else:
	not_pass = N-(A+B-C)
	print -1 if not_pass < 1 else not_pass