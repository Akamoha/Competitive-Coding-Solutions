for _ in range(int(input())):
    C = bin(int(input()))[2:]
    A, B = '10'
    for bit in C[1:]:
        A += '10'[int(bit)]
        B += '1'
    print(int(A, 2)*int(B, 2))