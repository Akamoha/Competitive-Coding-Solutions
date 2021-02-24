def opposite(x, a, b):
    return b if x == a else a

def solve(S, a, b):
    ht = {}
    c = {a:0, b:0}
    for s in S:
        ht[s] = 1
    for s in S:
        if opposite(s[0], a, b)+s[1:] not in ht:
            c[s[0]] += 1
    return 2*c[a]*c[b]

for _ in range(int(input())):
    N = int(input())
    S = input().split()
    ht = {}
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for l in alphabet:
        ht[l] = []
    for s in S:
        ht[s[0]].append(s)
        
    ans = 0
    for i in range(26):
        for j in range(i+1, 26):
            a, b = alphabet[i], alphabet[j]
            ans += solve(ht[a]+ht[b], a, b)
    print(ans)