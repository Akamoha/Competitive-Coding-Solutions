#include<stdio.h>
unsigned long int split(unsigned long int n) {
	if(n/4 + n/3 + n/2 < n)
		return (n);
	else
		return (split(n/4) + split(n/3) + split(n/2));
}
		
		
int main() {
	unsigned long int n;
	while(scanf("%lu",&n)!=EOF) {
		printf("%lu\n",split(n));
	}
	return 0;
}