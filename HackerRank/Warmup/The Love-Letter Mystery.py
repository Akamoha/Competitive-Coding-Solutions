T = int(raw_input())
for i in range(T):
    str = raw_input()
    score = 0
    endj = len(str)-1
    j = 0
    while j < endj:
        score += abs(ord(str[endj]) - ord(str[j]))
        j += 1
        endj -= 1
    print score
        