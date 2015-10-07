#include<stdio.h>
int main() {
	int answer = 0;
	int input, t, i;
	scanf("%d", &t);
	for(i = 0; i < t; i++) {
		scanf("%d", &input);
		answer ^= input;
	}
	printf("%d", answer);
	return 0;
}