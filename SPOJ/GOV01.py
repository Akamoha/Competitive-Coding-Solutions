def p(A,N):
 if N==1:
  return A
 x,z,s=p(A,N/2),zip,sum
 y = [[s((a*b)%M for a,b in z(r,c)) for c in z(*x)] for r in x];return [[s((a*b)%M for a,b in z(r,c)) for c in z(*y)] for r in A] if N%2 else y
for _ in range(input()):
 n,M=map(int,raw_input().split());print((p([[1,1],[1,0]],n+3))[0][0]-3%M)%M