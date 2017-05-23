#include <stdio.h>
 
long long finalCount = 0;
long long k;
int count = 0;
long long arr[30];
 
void getSolution(int currIndex, long long product) {
	
	if(product > k)
		return;
 
	// Base case
	if(currIndex == count) {
		finalCount++;
		return;
	}
 
	// Ignore
	getSolution(currIndex+1, product);
 
	// Use
	long long newProduct = product*arr[currIndex];
	if(newProduct/arr[currIndex] == product)	// Only send if there is no overflow
		getSolution(currIndex+1, newProduct);
}
 
int main() {
	int n;
	scanf("%d %lld", &n, &k);
 
 
	int numberOfOnes = 0;
	while(n--) {
		long long x;
		scanf("%lld", &x);
		if(x == 1)
			numberOfOnes++;
		else if (x <= k)
			arr[count++] = x;
	}
 
	getSolution(0, 1);
 
	long long subsequencesOfOnes = 1;
	subsequencesOfOnes = subsequencesOfOnes << numberOfOnes;
	long long nonEmptySusbsequencesOfOnes = subsequencesOfOnes -1;
 
	long long ans;
	if(k == 1) {
		ans = nonEmptySusbsequencesOfOnes;
	} else {
		ans = finalCount - 1;	// remove the empty subsequence
		ans = ans*subsequencesOfOnes + nonEmptySusbsequencesOfOnes;	// number of subsequences of 1 (includes empty subsequences) which don't affect product
	}
	printf("%lld\n", ans);
	return 0;
} 