T = int(raw_input())
for i in range(T):
    A,B = map(int, raw_input().split())
    n = 1
    count = 0
    i = 1
    while n <= B:
        if n >= A:
            count += 1
        n += (2*i + 1)
        i += 1
    print count