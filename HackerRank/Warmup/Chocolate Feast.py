T = int(raw_input())
for i in range (0,T):
    N,C,M = [int(x) for x in raw_input().split(' ')]
    wrappers = int(N/C)
    answer = wrappers
    while(wrappers >= M):
        answer += int(wrappers/M)
        wrappers = (wrappers % M) + int(wrappers/M)
    print answer