#include<stdio.h>
#include<iostream>
#include<stdint.h>

using namespace std;

long long int nCr(int n, int r){
    if(r > n - r) {
		r = n - r;
	}
    
    long long int ans = 1;
    int i;
	
    for(i = 0; i < r; i++) {
		ans = ans * (n-i)/(i+1);
    }
	
    return ans;
}

int main() {
	int T, t;
	long long int n, k;
	scanf("%d", &T);
	for(t = 0; t < T; t++) {
		scanf("%lld %lld", &n, &k);
		printf("%lld\n",nCr(n-1, k-1));
	}
	return 0;
}