T = int(raw_input())
for _ in range(T):
    N, K = map(int, raw_input().split())
    A = map(int, raw_input().split())
    count = 0
    for a in A:
        if a <= 0:
            count += 1
    if count >= K:
        print "NO"
    else:
        print "YES"
