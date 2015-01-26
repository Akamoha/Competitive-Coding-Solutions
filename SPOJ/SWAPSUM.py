n, q = map(int, raw_input().split())
A = map(int, raw_input().split())
sum = 0
CSA = []
for i in range(n):
    sum += A[i]
    CSA.append(sum)
    
for _ in range(q):
    tp, l, r = map(int, raw_input().split())
    if tp == 2:
        if l-2 >= 0:
            print CSA[r-1] - CSA[l-2]
        else:
            print CSA[r-1]
    else:
        for i in range(l-1, r-1, 2):
            if i != 0:
                CSA[i] += CSA[i+1] - CSA[i] - CSA[i] + CSA[i-1]
            else:
                CSA[i] = CSA[i+1] - CSA[i]