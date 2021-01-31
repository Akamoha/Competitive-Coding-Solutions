for _ in range(int(input())):
    input()
    A = list(map(int, input().split()))
    A = [a%2 for a in A]
    print(min(A.count(0), A.count(1)))