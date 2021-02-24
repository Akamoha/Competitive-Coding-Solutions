for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    print(2*(max(A)-min(A)))