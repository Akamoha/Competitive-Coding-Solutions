#include<bits/stdc++.h>

using namespace std;

vector<int> check(vector<int> A, int x) {
	multiset<int> M (A.begin(), A.end());
	vector<int> res;
	int mx, other;
	while(!M.empty()) {
		mx = *M.rbegin();
		auto it1 = M.find(mx);
		M.erase(it1);
		
		other = x-mx;
		if(M.find(other) == M.end()) {
			res.clear();
			return res;
		}
		auto it2 = M.find(other);
		M.erase(it2);

		res.push_back(mx);
		res.push_back(other);
		
		x = max(mx, other);
	}
	return res;
}

void solve() {
	int n;
	cin>>n;
	vector<int> A(2*n);
	for(int i = 0; i < 2*n; i++) {
		cin>>A[i];
	}
	sort(A.begin(), A.end());
	int mx = A[2*n-1];
	for(int i = 0; i < 2*n-1; i++) {
		vector<int> res = check(A, mx+A[i]);
		if(res.size()) {
			cout<<"YES"<<endl<<mx+A[i]<<endl;
			for(int j = 0; j < res.size(); j += 2) {
				cout<<res[j]<<" "<<res[j+1]<<endl;
			}
			return;
		}
	}
	cout<<"NO"<<endl;
	return;
}

int main() {
	int t;
	cin>>t;
	for(int i = 0; i < t; i++) {
		solve();
	}
	return 0;
}