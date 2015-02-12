T = int(raw_input())
for i in range(T):
    N = int(raw_input())
    str = "5"*N
    flag = 1
    for i in range(N+1):
        num = int(str)
        if (N-i) % 3 == 0 and i % 5 == 0:
            print num
            flag = 0
            break
        str = str[:(N-1-i)] + "3"*(i+1)
    if flag == 1:
        print -1