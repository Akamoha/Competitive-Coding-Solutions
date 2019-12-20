def num_iter(A, B):
    if int(B, 2) == 0:
        return 0
    if int(A, 2) == 0:
        return 1
    A = A[::-1]
    B = B[::-1]
    if len(A) > len(B):
        B += '0'*(len(A)-len(B))
    else:
        A += '0'*(len(A)-len(B))
    c = -1
    mxc = 0
    base = 0
    for i in range(min(len(A), len(B))):
        if A[i] == B[i] == '1':
            c = 0
            base = 2
        elif A[i] == B[i] == '0':
            c = -1
        else:
            base = max(base, 1)
            if c >= 0:
                c += 1
                mxc = max(mxc, c)
    return base+mxc
        
for _ in range(int(input())):
    A = input()
    B = input()
    print(num_iter(A, B))