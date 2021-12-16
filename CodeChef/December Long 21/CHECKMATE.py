import sys
input = sys.stdin.readline

def get_ints():
    return list(map(int, input().split()))
    
def execute_check(xk, yk, x1, y1, x2, y2):
    all_moves = [
        (xk, y1, x2, y2),
        (x1, yk, x2, y2),
        (x1, y1, xk, y2),
        (x1, y1, x2, yk)
    ]
    if y1 != y2 and x1 != x2:
        return all_moves
    elif y1 == y2:
        if x1 < xk < x2 or x2 < xk < x1:
            return all_moves
        elif abs(x1 - xk) < abs(x2 - xk):
            return [
                (xk, y1, x2, y2),
                (x1, yk, x2, y2),
                (x1, y1, x2, yk)
            ]
        else:
            return [
                (x1, yk, x2, y2),
                (x1, y1, xk, y2),
                (x1, y1, x2, yk)
            ]
    else:
        if y1 < yk < y2 or y2 < yk < y1:
            return all_moves
        elif abs(y1 - yk) < abs(y2 - yk):
            return [
                (xk, y1, x2, y2),
                (x1, yk, x2, y2),
                (x1, y1, xk, y2)
            ]
        else:
            return [
                (xk, y1, x2, y2),
                (x1, y1, xk, y2),
                (x1, y1, x2, yk)
            ]
        
def move_king(xk, yk, x1, y1, x2, y2):
    boards = [
        (xk+xmove, yk+ymove, x1, y1, x2, y2) for xmove in [-1, 0, 1] for ymove in [-1, 0, 1] if xmove != 0 or ymove != 0
    ]
    return list(filter(lambda x: (0 < x[0] < 9)&(0 < x[1] < 9) , boards))

def is_check(board):
    xk, yk, x1, y1, x2, y2 = board
    if x1 != xk and y1 == yk:
        return True
    elif x1 == xk and y1 != yk:
        return True
    elif x2 != xk and y2 == yk:
        return True
    elif x2 == xk and y2 != yk:
        return True
    return False

def is_checkmate(xk, yk, blackpos):
    x1, y1, x2, y2 = blackpos
    for board in move_king(xk, yk, x1, y1, x2, y2):
        if not is_check(board):
            return False
    return True
    
for _ in range(int(input())):
    xk, yk = get_ints()
    x1, y1 = get_ints()
    x2, y2 = get_ints()
    for blackpos in execute_check(xk, yk, x1, y1, x2, y2):
        if is_checkmate(xk, yk, blackpos):
            print("YES")
            break
    else:
        print("NO")