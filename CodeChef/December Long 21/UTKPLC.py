for _ in range(int(input())):
    A, B, C = input().split()
    ht = {}
    ht[A] = 3
    ht[B] = 2
    ht[C] = 1
    X, Y = input().split()
    if ht[X] > ht[Y]:
        print(X)
    else:
        print(Y)