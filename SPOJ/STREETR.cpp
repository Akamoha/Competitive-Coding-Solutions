#include<stdio.h>
#include<iostream>

using namespace std;

long long int gcd(long long int a, long long int b) {
    return b == 0 ? a : gcd(b, a % b);
}

int main() {
	long long int N, c1, c2, cn, d, c, i;
	scanf("%lld", &N);
	scanf("%lld", &c1);
	scanf("%lld", &c2);
	d = c2-c1;
	for(i = 0; i < N-3; i++) {
		scanf("%lld", &c);
		d = gcd(d, c-c2);
		c2 = c;
	}
	scanf("%lld", &cn);
	d = gcd(d, cn-c2);
	printf("%lld\n", (cn-c1)/d + 1 - N);
	return 0;
}