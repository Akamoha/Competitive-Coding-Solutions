n = 400

prime = [True for i in range(n+1)]
p = 2
while (p * p <= n):
    if (prime[p] == True):
        for i in range(p * p, n+1, p):
            prime[i] = False
    p += 1

P = []
for p in range(2, n+1):
    if prime[p]:
        P.append(p)

squaredP = [p**2 for p in P if p**2 < 400]
smallP = [p for p in P if p < 250]

for t in range(int(input())):
    for psq in squaredP:
        print(psq)
        ans = input()
        if ans == "YES":
            print("0")
            break
    else:
        c = 0
        for p in smallP:
            print(p)
            ans = input()
            if ans == "YES":
                c += 1
                if c == 2:
                    print("0")
                    break
        else:
            print("1")