for _ in range(int(input())):
    R = list(map(int, input().split()))
    I, E = R.count(1), R.count(2)
    if I > E:
        print("INDIA")
    elif E > I:
        print("ENGLAND")
    else:
        print("DRAW")