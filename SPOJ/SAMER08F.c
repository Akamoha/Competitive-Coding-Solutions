#include<stdio.h>
int numRecur(int N) {
	if(N==1)
		return 1;
	else
		return (numRecur(N-1) + 2*N - 1 + (N-1)*(N-1));
}
int main() {
	int N;
	while(1) {
		scanf("%d", &N);
		if(N==0)
			break;
		else
			printf("%d", numRecur(N));
	}
	return 0;
}