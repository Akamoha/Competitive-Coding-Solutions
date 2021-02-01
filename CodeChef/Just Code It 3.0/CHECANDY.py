def isSubsetSum(stt, n, smm):
    subset =([[False for i in range(smm + 1)] 
            for i in range(n + 1)])

    for i in range(n + 1):
        subset[i][0] = True
         
    for i in range(1, smm + 1):
         subset[0][i]= False
             
    for i in range(1, n + 1):
        for j in range(1, smm + 1):
            if j<stt[i-1]:
                subset[i][j] = subset[i-1][j]
            if j>= stt[i-1]:
                subset[i][j] = (subset[i-1][j] or
                                subset[i - 1][j-stt[i-1]])
    return subset[n][smm]
    
for _ in range(int(input())):
    N = int(input())
    C = list(map(int, input().split()))
    print("Impressed" if isSubsetSum(C, N, sum(C)//2) else "Not Impressed")