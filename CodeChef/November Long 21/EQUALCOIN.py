for _ in range(int(input())):
    X, Y = list(map(int, input().split()))
    if Y%2 and X<2 or X%2:
        print('NO')
    else:
        print('YES')