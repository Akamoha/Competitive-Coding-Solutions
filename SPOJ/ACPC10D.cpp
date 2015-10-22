#include<stdio.h>
#include<iostream>
#include<limits.h>

using namespace std;

int min(int a, int b) {
	if(a < b) return a;
	return b;
}

int min(int a, int b, int c, int d) {
	return min(min(a, b), min(c, d));
}

int main() {
	int N, i, j, tc = 0;
	cin>>N;
	while(N > 0) {
		tc++;
		int A[N][3];
		for(i = 0; i < N; i++) {
			for(j = 0; j < 3; j++) {
				cin>>A[i][j];
			}
		}
		int DP[N-1][5];
		DP[0][0] = INT_MAX;		
		DP[0][1] = INT_MAX;
		DP[0][2] = A[0][1];
		DP[0][3] = A[0][1] + A[0][2];
		DP[0][4] = INT_MAX;

		for(i = 1; i < N; i++) {
			DP[i][0] = DP[i][4] = INT_MAX;
			for(j = 1; j < 4; j++) {
				DP[i][j] = A[i][j-1] + min(DP[i][j-1], DP[i-1][j-1], DP[i-1][j], DP[i-1][j+1]);
			}
		}

		printf("%d. %d\n", tc, DP[N-1][2]);
		cin>>N;
	}
	return 0;
}
