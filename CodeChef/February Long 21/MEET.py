def conv(time):
    h = int(time[:2])%12
    m = int(time[3:5])
    ap = time[-2:]
    ret = h*60 + m
    if ap == 'PM':
        ret += 12*60
    return ret

for _ in range(int(input())):
    P = conv(input())
    for __ in range(int(input())):
        LR = input()
        L = conv(LR[:8])
        R = conv(LR[9:])
        print(int(L <= P <= R), end='')
    print()