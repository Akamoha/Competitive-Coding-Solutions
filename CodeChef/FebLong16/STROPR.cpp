#include<stdio.h>
#include<iostream>

#define MOD 1000000007

using namespace std;

long long fast_pow(long long base, long long n,long long M) 
{
    if(n==0)
       return 1;
    if(n==1)
    return base;
    long long halfn=fast_pow(base,n/2,M);
    if(n%2==0)
        return ( halfn * halfn ) % M;
    else
        return ( ( ( halfn * halfn ) % M ) * base ) % M;
}
long long findMMI_fermat(long long n,long long M)
{
    return fast_pow(n,M-2,M);
}

int main() {
	int T, t;
	long long int N, x, M, i, ans, multiplier, iteration;
	long long int A[100001];
	scanf("%d", &T);
	for(t = 0; t < T; t++) {
		scanf("%lld %lld %lld", &N, &x, &M);
		for(i = 0; i < N; i++) {
			scanf("%lld", &A[i]);
		}
		if(x == 1) {
			printf("%lld\n", (A[0]%MOD));
		} else if(x == 2) {
			printf("%lld\n", (((M%MOD)*(A[0]%MOD))%MOD + (A[1])%MOD)%MOD);
		} else {
			ans = A[x-1]%MOD;
			multiplier = 1;
			iteration = 0;
			//cout<<multiplier<<endl;
			for(i = x-1; i >= 1; i--) {
				multiplier = ( ( ((multiplier%MOD)*((M%MOD+iteration%MOD)%MOD))%MOD) * ((findMMI_fermat(iteration+1,MOD)%MOD)%MOD))%MOD;
				ans = ((ans%MOD) + ((multiplier%MOD)*(A[i-1]%MOD))%MOD)%MOD;
				iteration++;
				//cout<<multiplier<<endl;
			}
			printf("%lld\n", ans%MOD);
		}
	}
	return 0;
}