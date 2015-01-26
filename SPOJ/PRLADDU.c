#include<stdio.h>
int main() {
	int T;
	long long int D[10000], units;
	int i,j,x,n;
	scanf("%d", &T);
	for(x=0;x<T;x++) {
		scanf("%d", &n);
		for(i=0;i<n;i++) {
			scanf("%lld", &D[i]);
		}
		i = 0;
		units = 0;
		while (i < n) {
			if (D[i] < 0) {
				j = 0;
				while (D[i] < 0) {
					if (D[j] > 0) {
						if (D[j] > (-1)*(D[i])) {
							if(j>i)
								units += (j-i) * (-1)*(D[i]);
							else
								units += (i-j) * (-1)*(D[i]);
							D[j] += D[i];
							D[i] = 0;
						}
						else {
							if(j>i)
								units += (j-i) * D[j];
							else
								units += (i-j) * D[j];
							D[i] += D[j];
							D[j] = 0;
						}
					}
					j++;
				}
			}
			i++;
		}
	printf("%lld\n", units);
	}
}