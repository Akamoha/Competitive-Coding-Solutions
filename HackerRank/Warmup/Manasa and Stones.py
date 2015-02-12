T = int(raw_input())
for i in range(T):
    n = int(raw_input())
    a = int(raw_input())
    b = int(raw_input())
    arr = []
    for j in range(n):
        arr.append(a*(n-1-j) + b*j)
    arr = list(set(arr))
    arr.sort()
    for printed in arr:
        print printed,
    print