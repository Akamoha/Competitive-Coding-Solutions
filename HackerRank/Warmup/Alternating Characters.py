T = int(raw_input())
for _ in range(T):
    s = raw_input()
    count = 0
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            count += 1
    print count