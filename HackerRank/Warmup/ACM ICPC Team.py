def topics(A, B):
    count = 0
    for k in range(len(A)):
        if A[k] == '1' or B[k] == '1':
            count += 1
    return count

N, M = map(int, raw_input().split())
matrix = []
for _ in range(N):
    matrix.append(raw_input())
    
tList = []
for i in range(N - 1):
    for j in range(i + 1, N):
        tList.append(topics(matrix[i], matrix[j]))
m = max(tList)
print m
print tList.count(m)
            