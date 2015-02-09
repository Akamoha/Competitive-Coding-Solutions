S1 = raw_input()
S2 = raw_input()
lenS1 = len(S1)
lenS2 = len(S2)
count = 0
for i in range(lenS1-lenS2+1):
    if S2 == S1[i:i+lenS2]:
        count += 1
print count
