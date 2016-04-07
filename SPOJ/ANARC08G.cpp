#include<stdio.h>
#include<iostream>

using namespace std;

int main() {
	int N, i, j, temp, A, tc, B;
	int M[1001][1001];
	scanf("%d", &N);
	tc = 1;
	while(N) {
		A = B = 0;
		for(i = 0; i < N; i++) {
			for(j = 0; j < N; j++) {
				scanf("%d", &M[i][j]);
				B += M[i][j];
			}
		}
		for(i = 0; i < N; i++) {
			temp = 0;
			for(j = 0; j < N; j++) {
				temp += M[i][j] - M[j][i];
			}
			if(temp > 0) {
				A += temp;
			}
		}
		printf("%d. %d %d\n", tc, B, A);
		scanf("%d", &N);
		tc++;
	}
	return 0;
}