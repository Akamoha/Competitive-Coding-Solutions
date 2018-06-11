#include<stdio.h>
#include<iostream>

using namespace std;

int main() {
	int T, t, i;
	unsigned long long int N, M, K, k, r, c;
	double count;
	scanf("%d", &T);
	for(t = 0; t < T; t++) {
		count = 0.0;
		scanf("%llu %llu %llu", &N, &M, &K);
		for(i = 0; i < K; i++) {
			scanf("%llu", &k);
			r = (k-1)/M;
			c = (k-1)%M;
			count += ((M-c)*1.0/N) * ((r+1)*1.0/M) * ((N-r)*1.0/(N+1)) * ((c+1)*1.0/(M+1)) * 4.0;
		}
		printf("%0.15f\n", count*1.0000000);
	}
	return 0;
}