for _ in range(int(input())):
    X, Y, A, B, K = list(map(int, input().split()))
    p, d = X+K*A, Y+K*B
    if p==d:
        print("SAME PRICE")
    elif p>d:
        print("DIESEL")
    else:
        print("PETROL")