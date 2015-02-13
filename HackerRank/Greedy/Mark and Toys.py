N, K = map(int, raw_input().split())
A = map(int, raw_input().split())
A.sort()
count = 0
for a in A:
    if K-a >= 0:
        count += 1
        K -= a
    else:
        break
print count