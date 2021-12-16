def winner(a, b):
    if a == b:
        return a
    elif a == "R" and b == "P":
        return "P"
    elif a == "R" and b == "S":
        return "R"
    elif a == "P" and b == "S":
        return "S"
    else:
        return winner(b, a)

for _ in range(int(input())):
    N = int(input())
    S = input()[::-1]
    A = [{p:p for p in "RPS"}]
    for m in S:
        A.append({p:A[-1][winner(p, m)] for p in "RPS"})
    print(''.join([A[i][S[i]] for i in range(N)])[::-1])