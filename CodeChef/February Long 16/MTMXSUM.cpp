#include<iostream>
#include<stdio.h>

using namespace std;

#define MOD 1000000007

int main() {
	long long int N, sumA, sumB, i;
	long long int A[100001], B[100001];
	scanf("%lld", &N);
	sumA = 0;
	sumB = 0;
	for(i = 0; i < N; i++) {
		scanf("%lld", &A[i]);
		A[i] += i+1;
		sumA = (sumA%MOD + A[i]%MOD)%MOD;
	}
	for(i = 0; i < N; i++) {
		scanf("%lld", &B[i]);
		B[i] += i+1;
		sumB = (sumB%MOD + B[i]%MOD)%MOD;
	}
	while(N > 0) {
		printf("%lld ", ((sumA%MOD)*(sumB%MOD))%MOD);
		sumA = 0;
		sumB = 0;
		for(i = 0; i < N-1; i++) {
			A[i] = max(A[i], A[i+1]);
			sumA += A[i];
			B[i] = max(B[i], B[i+1]);
			sumB += B[i];
		}
		N--;
	}
	return 0;
}