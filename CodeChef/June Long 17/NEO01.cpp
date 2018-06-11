#include <bits/stdc++.h>

using namespace std;

int main() {
	int T, N, t, i, a;
	long long int prev, leftSum, rightSum;
	vector<int> A;
	vector<long long int> leftCSA, rightCSA;
	cin>>T;
	for(t = 0; t < T; t++) {
		A.clear();
		leftCSA.clear();
		rightCSA.clear();
		cin>>N;
		for(i = 0; i < N; i++) {
			cin>>a;
			A.push_back(a);
		}
		sort(A.begin(), A.end());
		leftSum = 0;
		rightSum = 0;
		for(i = 0; i < N; i++) {
			leftSum += A[i];
			leftCSA.push_back(leftSum);

			rightSum += A[N-i-1];
			rightCSA.push_back(rightSum);
		}
		// for(i = 0; i < N; i++) {
		// 	cout<<A[i]<<" ";
		// }
		// cout<<endl;
		// for(i = 0; i < N; i++) {
		// 	cout<<leftCSA[i]<<" ";
		// }
		// cout<<endl;
		// for(i = 0; i < N; i++) {
		// 	cout<<rightCSA[i]<<" ";
		// }
		// cout<<endl;

		prev = rightCSA[N-1]*N;
		for(i = 1; i < N; i++) {
			prev = max(prev, leftCSA[i-1] + rightCSA[N-i-1]*(N-i));
		}
		prev = max(prev, leftCSA[N-1]);
		cout<<prev<<endl;
	}
	return 0;
}