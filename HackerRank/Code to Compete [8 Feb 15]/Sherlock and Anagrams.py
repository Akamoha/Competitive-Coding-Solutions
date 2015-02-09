T = int(raw_input())
for _ in range(T):
    S = raw_input()
    HT = {}
    for letter in S:
        if letter in HT:
            HT[letter] += 1
        else:
            HT[letter] = 1
    count = 0
    for letter in HT:
        count += HT[letter]*(HT[letter]-1)/2
    for i in range(2,len(S)):
        HT = {}
        for j in range(len(S)-i+1):
            total = list(S[j:j+i])
            total.sort()
            total = str(total)
            #for letter in S[j:j+i]:
            #    total += (ord(letter) - 96)*103
            if total in HT:
                HT[total].append(S[j:j+i])
            else:
                HT[total] = []
                HT[total].append(S[j:j+i])
        for key in HT:
            count += len(HT[key])*(len(HT[key]) - 1)/2
    print count
