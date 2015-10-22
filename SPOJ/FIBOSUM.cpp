#include<stdio.h>
#include<iostream>
#define MOD 1000000007

using namespace std;

long long int abs(long long int a) {
	if(a < 0) {
		return -1*a;
	}
	return a;
}

void multiply(long long int A[][2], long long int B[][2], long long int C[][2]) {
	C[0][0] = (((A[0][0]%MOD)*(B[0][0])%MOD)%MOD + ((A[0][1]%MOD)*(B[1][0])%MOD)%MOD)%MOD;
	C[0][1] = (((A[0][0]%MOD)*(B[0][1])%MOD)%MOD + ((A[0][1]%MOD)*(B[1][1])%MOD)%MOD)%MOD;
	C[1][0] = (((A[1][0]%MOD)*(B[0][0])%MOD)%MOD + ((A[1][1]%MOD)*(B[1][0])%MOD)%MOD)%MOD;
	C[1][1] = (((A[1][0]%MOD)*(B[0][1])%MOD)%MOD + ((A[1][1]%MOD)*(B[1][1])%MOD)%MOD)%MOD;
}

void power(long long int A[2][2], long long int N, long long int ans[2][2]) {
	if(N == 1 || N == 0) {
		ans[0][0] = A[0][0];
		ans[0][1] = A[0][1];
		ans[1][0] = A[1][0];
		ans[1][1] = A[1][1];
		return;
	}
	long long int ApowNby2[2][2];
	power(A, N/2, ApowNby2);
	if(N % 2 == 0) {
		multiply(ApowNby2, ApowNby2, ans);
		return;
	}
	long long int middle[2][2];
	multiply(ApowNby2, A, middle);
	multiply(ApowNby2, middle, ans);
	return;
}

int main() {
	long long int T, t, N, M, i, j, ans[2][2], ans2[2][2];
	long long int matrix[2][2];
	long long int temp;
	matrix[0][0] = 1;
	matrix[0][1] = 1;
	matrix[1][0] = 1;
	matrix[1][1] = 0;
	scanf("%lld", &T);
	for(t = 0; t < T; t++) {
		scanf("%lld %lld", &N, &M);
		power(matrix, M+1, ans);
		for(i = 0; i < 2; i++) {
			for(j = 0; j < 2; j++) {
			}
		}
		power(matrix, N, ans2);
		for(i = 0; i < 2; i++) {
			for(j = 0; j < 2; j++) {
			}
		}
		if(ans[0][0]%MOD > ans2[0][0]%MOD) {
			cout<<abs(ans[0][0]-ans2[0][0])%MOD<<endl;
		} else {
			cout<<abs(ans[0][0]+MOD-ans2[0][0])%MOD<<endl;
		}
	}
	return 0;
}