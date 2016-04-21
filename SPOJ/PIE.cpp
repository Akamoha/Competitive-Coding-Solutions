#include<stdio.h>
#include<iostream>
#include<bits/stdc++.h>

#define PI 3.14159265358979323846264338327950

using namespace std;

vector<double> pies;
int T, N, F;

bool possible(double piesize) {
	int numpies = 0, i;
	for(i = N-1; i >= 0; i--) {
		numpies += pies[i]/piesize;
		if(numpies >= F+1)
			return true;
	}
	return false;
}

int main() {
	int t, i;
	scanf("%d", &T);
	int r;
	for(t = 0; t < T; t++) {
		pies.clear();
		scanf("%d", &N);
		scanf("%d", &F);
		for(i = 0; i < N; i++) {
			scanf("%d", &r);
			pies.push_back(PI*r*r);
		}
		sort(pies.begin(), pies.end());
		double low = 0.0, high = pies[N-1], mid;
		while(low <= high) {
			mid = (low+high)/2;
			if(possible(mid)) {
				low = mid+0.000001;
			} else {
				high = mid-0.000001;
			}
		}
		printf("%lf\n", mid);
	}
	return 0;
}