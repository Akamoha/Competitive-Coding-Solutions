T = int(raw_input())
for i in range (0,T):
    N = int(raw_input())
    height = 1
    for j in range(0,int(N/2)):
        height = 2*height + 1
    if (N%2 != 0):
        height = 2*height
    print height