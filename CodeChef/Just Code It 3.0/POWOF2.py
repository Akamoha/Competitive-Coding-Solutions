import math 

def solve(x):
    if x == 1:
        return 1
    if x%2:
        return 0
    l = math.log(x, 2)
    if l == int(l):
        return 1+solve(int(l))
    return 0
    
def solve2(x):
    if x%2:
        return 0
    l = math.log(x, 2)
    if l == int(l):
        return solve(int(l))
    return 0

for _ in range(int(input())):
    x = int(input())
    print(solve2(x))