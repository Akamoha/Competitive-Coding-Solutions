import sys

def take():
    global queries
    queries += 1
    return int(input())

def tries(i, j):
    return [(i+1, j),
            (i+1, j+1),
            (i+1, j),
            (i, j+1),
            (i+1, j),
            (i+1, j+1),
            (i+1, j)]
            
def letsgo(i, j, x, y):
    print(1, x, y, flush=True)
    Z = take()
    print(1, i, j, flush=True)
    Znext = take()
    if Znext > Z:
        return True, Znext
    if Znext < Z:
        print(1, i, j, flush=True)
        return True, take()
    return False, Znext

def fix(i, j, Z):
    print(1, i, j, flush=True)
    Znext = take()
    if Znext > Z:
        return Znext
    if Znext < Z:
        print(1, i, j, flush=True)
        return take()
    for x, y in tries(i, j):
        fixed, Z = letsgo(i, j, x, y)
        if fixed:
            return Z
        
for _ in range(int(input())):
    N, Q, K = list(map(int, input().split()))
    queries = 0
    if N == 2:
        fix(1, 1, K)
        print(2, flush=True)
        print(0,1, flush=True)
        print(1,0, flush=True)
    if N == 3:
        K = fix(1, 1, K)
        print(1, 1, 1, flush=True)
        K = take()
        K = fix(1, 2, K)
        print(1, 1, 2, flush=True)
        K = take()
        K = fix(2, 1, K)
        print(1, 2, 1, flush=True)
        K = take()
        K = fix(2, 2, K)
        print(2, flush=True)
        print(1,1,1, flush=True)
        print(1,0,1, flush=True)
        print(1,1,0, flush=True)
    if N == 4:
        K = fix(1, 1, K)
        K = fix(1, 3, K)
        K = fix(3, 1, K)
        print(1, 3, 2, flush=True)
        K = take()
        K = fix(3, 3, K)
        print(2, flush=True)
        print(0,1,0,1, flush=True)
        print(1,0,1,0, flush=True)
        print(0,0,0,1, flush=True)
        print(1,0,1,0, flush=True)
    take()