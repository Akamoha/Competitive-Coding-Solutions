for _ in range(int(input())):
    A, B = list(map('{:035b}'.format, map(int, input().split())))
    op = ''
    for i in range(len(A)):
        if B[i] == A[i]:
            op += A[i]
        else:
            op += '0'
            break
    for j in range(i+1, len(A)):
        op += '1'
    print(int(op, 2))