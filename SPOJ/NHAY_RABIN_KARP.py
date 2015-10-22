"""
NOTE: This Rabin Karp implementation gives TLE in Python, even after using pow(a,b,c) for modular exponentiation.
"""

q = 10**9 + 7
d = 26

while True:
	try:
		lite = input()
		
		P = raw_input()
		T = raw_input()

		p = 0
		t = 0
		
		n = len(T)
		m = len(P)

		h = pow(d, m-1, q)

		if n < m:
			print ""
			continue

		for i in range(m):
			p = (d*p + ord(P[i]))%q
			t = (d*t + ord(T[i]))%q

		for i in range(n-m+1):
			if t == p:
				if T[i:i+m] == P:
					print i
			if i+m < n:
				t = (d*(t-ord(T[i])*h) + ord(T[i+m]))%q
	except:
		break