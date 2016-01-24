#include<stdio.h>
#include<iostream>
#include<map>
using namespace std;
int main() {
	int n, i;
	map<int, long long int> h;
	h[1] = 5;
	for(i = 2; i <= 1000; i++) {
		h[i] = h[i-1] + 3*i + 1;
	}
	while(1) {
		scanf("%d",&n);
		if(n==0)
			return 0;
		printf("%d\n", h[n]);
	}
	return 0;
}