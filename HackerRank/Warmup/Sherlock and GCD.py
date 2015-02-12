def GCD(a,b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)
    
T = int(raw_input())
for i in range(T):
    N = int(raw_input())
    A = map(int, raw_input().split())
    g = reduce(GCD, A)
    if g == 1:
        print "YES"
    else:
        print "NO"