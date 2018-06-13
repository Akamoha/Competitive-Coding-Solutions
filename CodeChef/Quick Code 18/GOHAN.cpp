#include<bits/stdc++.h>

using namespace std;

int main() {
	int t, T, R, L, C, V;
	cin>>T;
	long double ans;
	for(int i = 0; i < T; i++) {
		cin>>R>>L>>C>>V;
		ans = 1-1.0*R*R*C/(4*L);
		cout<<fixed<<ans<<endl;
	}
	return 0;
}