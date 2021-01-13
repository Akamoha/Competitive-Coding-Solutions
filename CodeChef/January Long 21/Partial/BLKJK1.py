def read_input():
    return list(map(int, input().split()))

def zero():
    global N, X, Y, A
    s = 0
    for a in A:
        s += a
        if X <= s <= Y:
            return True
    return False
    
def cumsum():
    s = 0
    ret = []
    for a in A:
        ret.append(a+s)
        s += a
    return ret
    
def bsearch(t, l, r):
    global X, Y
    low, high = l, r
    mid = low + (high-low)//2
    while low < high:
        mid = low + (high-low)//2
        if mid == r:
            term = 0
        else:
            term = t
        if X <= CSA[mid] + term <= Y:
            return True
        elif CSA[mid] + term < X:
            low = mid+1
        else:
            high = mid
    return False

for _ in range(int(input())):
    N, X, Y = read_input()
    A = read_input()
    if zero():
        print(0)
        continue
    CSA = cumsum()
    for i in range(N):
        if CSA[i] > X:
            break
    for j in range(i+1):
        for k in range(max(i,j), N):
            if bsearch(A[k]-A[j], j, k):
                print(1)
                break
        else:
            continue
        break
    else:
        print(2)