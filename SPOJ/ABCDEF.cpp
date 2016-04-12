#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<bits/stdc++.h>
#define sd(x) scanf("%d", &x)
#define pdln(x) printf("%d\n", x);

using namespace std;

int main() {
	int N, i, j, k, ia = 0, ib = 0;
	int S[1001];
	vector<int> A, B;
	sd(N);
	for(i = 0; i < N; i++) {
		sd(S[i]);
	}
	for(i = 0; i < N; i++) {
		for(j = 0; j < N; j++) {
			for(k = 0; k < N; k++) {
				A.push_back(S[i]*S[j]+S[k]);
				if(S[i] != 0) {
					B.push_back(S[i]*(S[j]+S[k]));
				}
			}
		}
	}
	sort(A.begin(), A.end());
	sort(B.begin(), B.end());
	int low, high;
	long long int answer = 0;
	for(i = 0; i < A.size(); i++) {
		low = lower_bound(B.begin(), B.end(), A[i])-B.begin();
		high = upper_bound(B.begin(), B.end(), A[i])-B.begin();
		answer += (high-low);
	}
	printf("%lld\n", answer);
	return 0;
}