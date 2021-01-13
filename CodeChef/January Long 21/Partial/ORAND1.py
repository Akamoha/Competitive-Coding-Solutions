import sys
sys.setrecursionlimit(2147000000)

def read_input():
    return list(map(int, input().split()))
        
def DFS(s):
    global visited, wat
    visited[s] = 1
    wat += 1
    if wat >= 2048:
        return
    for a in A:
        if s|a not in visited:
            DFS(s|a)
    for b in B:
        if s&b not in visited:
            DFS(s&b)
            
for _ in range(int(input())):
    N, M = read_input()
    A = read_input()
    B = read_input()
    visited = {}
    wat = 0
    DFS(0)
    print(wat)