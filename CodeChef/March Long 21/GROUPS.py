for _ in range(int(input())):
    S = input()+'0'
    ans = 0
    prev = S[0]
    for cur in S[1:]:
        if prev != cur and prev == '1':
            ans += 1
        prev = cur
    print(ans)