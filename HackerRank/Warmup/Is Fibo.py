T = int(raw_input())
for i in range(T):
    N = int(raw_input())
    a = 0
    b = 1
    fib = 0
    while(N > fib):
        fib = a+b
        a = b
        b = fib
        if N == fib:
            print "IsFibo"
            break
    if N < fib:
        print "IsNotFibo"