#!/bin/python

# Complete the function below.


def  maxXor( l,  r):
    max = 0
    for i in range(l,r+1):
        for j in range(l,r+1):
            if i^j > max:
                max = i^j
    return max
    

_l = int(raw_input());


_r = int(raw_input());

res = maxXor(_l, _r);
print(res)