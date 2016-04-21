#include<iostream>
#include<stdio.h>
#include<bits/stdc++.h>

#define sd(x) scanf("%d", &x)

using namespace std;

int n;
vector<int> A, B;
vector<pair<int, int> > C;

int solve() {
	int i, j, ans = 0;
	vector<int> lis;
	for(i = 0; i < n; i++) {
		lis.push_back(1);
	}
	for(i = 0; i < n; i++) {
		for(j = i-1; j >= 0; j--) {
			if(C[j].second <= C[i].second) {
				lis[i] = max(lis[i], lis[j]+1);
			}
		}
		ans = max(ans, lis[i]);
	}
	return ans;
}

int main () {
	int T, t, i, x;
	sd(T);
	for(t = 0; t < T; t++) {
		sd(n);
		A.clear();
		B.clear();
		C.clear();
		for(i = 0; i < n; i++) {
			sd(x);
			A.push_back(x);
		}
		for(i = 0; i < n; i++) {
			sd(x);
			B.push_back(x);
		}
		for(i = 0; i < n; i++) {
			C.push_back(make_pair(A[i], B[i]));
		}
		sort(C.begin(), C.end());
		printf("%d\n", solve());
	}
	return 0;
}