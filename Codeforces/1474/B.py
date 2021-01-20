import bisect as bi

n = 10**6

prime = [True for i in range(n+1)] 
p = 2
while (p * p <= n): 
      
    # If prime[p] is not changed, then it is a prime 
    if (prime[p] == True): 
          
        # Update all multiples of p 
        for i in range(p * p, n+1, p): 
            prime[i] = False
    p += 1
  
P = []
for p in range(2, n+1): 
    if prime[p]: 
        P.append(p)

for _ in range(int(input())):
    d = int(input())
    div1 = P[bi.bisect_left(P, 1+d)]
    div2 = P[bi.bisect_left(P, div1+d)]
    print(div1*div2)