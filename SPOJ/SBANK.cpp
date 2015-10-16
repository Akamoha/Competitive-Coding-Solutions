#include<stdio.h>
#include<iostream>
#include<map>

using namespace std;

int main() {
	int T, t, N, i;
	string s;
	map<string, int> HT;
	map<string, int>::iterator it;
	cin>>T;
	for(t = 0; t < T; t++) {
		scanf("%d", &N);
		HT.clear();
		getline(cin, s);
		for(i = 0; i < N; i++) {
			getline(cin, s);
			if(HT.find(s) != HT.end()) {
				HT[s]++;
			}	
			else {
				HT[s] = 1;
			}
		}
		for(it = HT.begin(); it != HT.end(); it++) {
			cout<<it->first<<" "<<it->second<<endl;
		}
		cout<<endl;
		if(t != T-1)
			getline(cin, s);
	}
	return 0;
}