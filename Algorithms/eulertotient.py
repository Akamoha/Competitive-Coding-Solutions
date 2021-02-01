from math import gcd

def phi(n): 
    result = n;  

    p = 2;  
    while(p * p <= n): 
        if (n % p == 0):  
            while (n % p == 0): 
                n = int(n / p); 
            result -= int(result / p); 
        p += 1; 
  
    if (n > 1): 
        result -= int(result / n); 
    return result 