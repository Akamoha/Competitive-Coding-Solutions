def ispower(n, base): 

    if n == base:
        return True

    if base == 1:
        return False

    temp = base

    while (temp <= n):
        if temp == n:
            return True
        temp *= base

    return False
	
	
n = int(raw_input())
if n == 0 or n == 1 or ispower(n, 2):
	print "TAK"
else:
	print "NIE"