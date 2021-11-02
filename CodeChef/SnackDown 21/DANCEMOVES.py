for _ in range(int(input())):
    X, Y = list(map(int, input().split()))
    if Y%2 == X%2:
        print((Y-X)//2 if Y > X else X-Y)
    else:
        print((Y+1-X)//2+1 if Y > X else X-Y)