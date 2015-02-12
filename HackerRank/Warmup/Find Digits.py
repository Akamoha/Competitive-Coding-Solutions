T = int(raw_input())
for i in range(T):
    N = int(raw_input())
    count = 0
    ori = N
    while N > 0:
        digit = N % 10
        if digit != 0 and ori % digit == 0:
            count += 1
        N /= 10
    print count