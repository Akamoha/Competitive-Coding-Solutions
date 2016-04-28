#include<bits/stdc++.h>

#define sd(x) scanf("%d", &x);

using namespace std;

int N;
vector<int> A;
unordered_map<int, long long int> HT;

long long int max(long long int a, long long int b, long long int c) {
	return max(a, max(b, c));
}

long long int solve(int x) {
	if(x >= N)
		return 0;
	if(N-x == 1)
		return A[x];
	if(N-x == 2)
		return A[x]+A[x+1];
	if(N-x == 3)
		return A[x]+A[x+1]+A[x+2];
	if(HT.find(x) == HT.end())
		HT[x] = max(A[x]+solve(x+2), A[x]+A[x+1]+solve(x+4), A[x]+A[x+1]+A[x+2]+solve(x+6));
	return HT[x];
}

int main() {
	int T, t, x, i;
	sd(T);
	for(t = 0; t < T; t++) {
		sd(N);
		A.clear();
		HT.clear();
		for(i = 0; i < N; i++) {
			sd(x);
			A.push_back(x);
		}
		if(N == 1)
			printf("%d\n", A[0]);
		else if(N == 2)
			printf("%d\n", A[0]+A[1]);
		else if(N == 3)
			printf("%d\n", A[0]+A[1]+A[2]);
		else
			printf("%lld\n", max(A[0]+solve(2), A[0]+A[1]+solve(4), A[0]+A[1]+A[2]+solve(6)));
		}
}