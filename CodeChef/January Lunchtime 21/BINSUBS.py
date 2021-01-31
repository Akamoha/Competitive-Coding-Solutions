import sys
sys.setrecursionlimit(2147000000)

def solve(i):
    if i == N-1:
        return int(s[i] == '0')
    if s[i] == '0':
        return solve(i+1)
    return min(1+solve(i+1), C[i])

for _ in range(int(input())):
    N = int(input())
    s = '0'+input()+'1'
    N = len(s)-2
    if N+1-s[::-1].index('0') < s.index('1'):
        print('0')
        continue
    s = s[1:-1]
    C = [0 for _ in range(N)]
    c = 0
    for i in range(N-1, -1, -1):
        c += int(s[i] == '0')
        C[i] = c
    print(min(solve(0), s.count('0'), s.count('1')))