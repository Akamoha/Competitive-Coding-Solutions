def solve(s, t):
    i, j = 0, 0
    ls, lt = len(s), len(t)
    ans = ''
    while True:
        if s[i] != t[j]:
            return -1
        ans += s[i]
        i += 1
        j += 1
        if i == ls and j == lt:
            return ans
        if i == ls:
            i = 0
        if j == lt:
            j = 0

for _ in range(int(input())):
    s = input()
    t = input()
    print(solve(s, t))