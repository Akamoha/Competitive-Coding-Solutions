import sys
sys.setrecursionlimit(2000000000)

MOD = 10**9+7

def NSLGTR(i):
	if N-i == 1:
		return ord('Z')-ord(s[i])
	return ((NSLGTR(i+1)%MOD*26)%MOD + ord('Z')-ord(s[i]))%MOD

def NSLGT(i):
	if N-i == 1:
		return ord('Z')-ord(s[i])
	return ((NSLGT(i+1)%MOD) + ((ord('Z')-ord(s[i]))*(pow(26, (N-i-1), MOD)))%MOD)%MOD
	
def solve(i):
	if N-i == 1:
		return ord('Z')-ord(s[i])
	return ((solve(i+1)%MOD) + ((ord('Z')-ord(s[i]))*(1+NSLGTR(i+1))%MOD)%MOD)%MOD

s = raw_input()
N = len(s)
print solve(0)%MOD