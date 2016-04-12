#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<bits/stdc++.h>

#define sd(x) scanf("%d", &x)
using namespace std;

int A[5000], B[5000], C[5000], D[5000];
int main() {
	int n, i, j, inp;
	vector<int> E, F;
	sd(n);
	for(i = 0; i < n; i++) {
		sd(A[i]);
		sd(B[i]);
		sd(C[i]);
		sd(D[i]);
	}
	for(i = 0; i < n; i++) {
		for(j = 0; j < n; j++) {
			E.push_back(A[i]+B[j]);
		}
	}
	for(i = 0; i < n; i++) {
		for(j = 0; j < n; j++) {
			F.push_back(C[i]+D[j]);
		}
	}
	sort(E.begin(), E.end());
	sort(F.begin(), F.end());
	long long int ans = 0;
	int low, high;
	for(i = 0; i < E.size(); i++) {
		low = lower_bound(F.begin(), F.end(), -1*E[i])-F.begin();
		high = upper_bound(F.begin(), F.end(), -1*E[i])-F.begin();
		ans += (high-low);
	}
	printf("%lld\n", ans);
	return 0;
}