#include<stdio.h>
#include<iostream>

using namespace std;

int main() {
  long long int P, p, i, j, N, n, sum, last = 0;
  long long int DP[11][64];
  for(i = 0; i < 11; i++) {
    for(j = 1; j < 64; j++) {
      DP[i][j] = -1;
    }
  }
  for(i = 0; i < 10; i++) {
    DP[i][0] = 1;
  }
  DP[10][0] = 10;
  scanf("%lld", &P);
  for(p = 0; p < P; p++) {
    scanf("%lld %lld", &n, &N);
    if(DP[10][N-1] != -1) {
      printf("%lld %lld\n", n, DP[10][N-1]);
    } else {
      for(j = last+1; j < N; j++) {
        DP[0][last+1] = DP[10][last];
        sum = DP[0][last+1];
        for(i = 1; i < 10; i++) {
          DP[i][j] = DP[i-1][j] - DP[i-1][j-1];
          sum += DP[i][j];
        }
        DP[10][j] = sum;
        last++;
      }
      printf("%lld %lld\n", n, DP[10][N-1]);
    }
  }
  return 0;
}
