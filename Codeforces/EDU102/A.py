for _ in range(int(input())):
    n, d = list(map(int, input().split()))
    A =  list(map(int, input().split()))
    if max(A) <= d:
        print('yes')
    elif n == 1:
        print('no')
    elif n == 2:
        print('no')
    else:
        A.sort()
        if A[0]+A[1] <= d:
            print('yes')
        else:
            print('no')