#include<bits/stdc++.h>

using namespace std;

int main() {
	int t, n;
	string b;
	cin>>t;
	for(int tt = 0; tt < t; tt++) {
		cin>>n>>ws;
		getline(cin, b);
		char prev = '0';
		for(int i = 0; i < n; i++) {
			if(b[i] == '0') {
				if(prev == '0') {
					cout<<'1';
					prev = '1';
				} else if(prev == '1') {
					cout<<'0';
					prev = '0';
				} else {
					cout<<'1';
					prev = '1';
				}
			} else {
				if(prev == '0') {
					cout<<'1';
					prev = '2';
				} else if(prev == '1') {
					cout<<'1';
					prev = '2';
				} else {
					cout<<'0';
					prev = '1';
				}
			}
		}
		cout<<endl;
	}
	return 0;
}