#include<stdio.h>
#include<math.h>

int numdiv(int N) {
	int ans = 0, i;
	for(i = 1; i <= sqrt(N); i++) {
		if(N % i == 0) {
			ans += 2;
			if(N/i == i) {
				ans--;
			}
		}
	}
	return ans;
}

int gcd(int A, int B) {
	if(B == 0) {
		return A;
	}
	return gcd(B, A%B);
}

int comdiv(int A, int B) {
	return numdiv(gcd(A, B));
}

int main() {
	int T, t, A, B;
	scanf("%d", &T);
	for(t = 0; t < T; t++) {
		scanf("%d%d", &A, &B);
		printf("%d\n", comdiv(A, B));
	}
	return 0;
}