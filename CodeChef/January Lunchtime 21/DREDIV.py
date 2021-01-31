def odd(k):
    if k%2:
        return k
    return odd(k//2)

for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    A = list(map(int, input().split()))
    ok = odd(k)
    for a in A:
        if a%ok:
            print("NO")
            break
    else:
        print("YES")