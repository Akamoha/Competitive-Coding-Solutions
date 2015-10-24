#include<stdio.h>
#include<iostream>

using namespace std;

int DP[6101][6101];

int LCS(string S, int len) {
	int i, j;
	for(i = 0; i < len + 1; i++) {
		DP[0][i] = 0;
		DP[i][0] = 0;
	}
	for(i = 1; i < len + 1; i++) {
		for(j = 1; j < len + 1; j++) {
			if(S[len-i] == S[j-1]) {
				DP[i][j] = DP[i-1][j-1] + 1;
			} else {
				DP[i][j] = max(DP[i-1][j], DP[i][j-1]);
			}
		}
	}
	return DP[len][len];
}

int main() {
	string S;
	int T, t;
	scanf("%d", &T);
	getline(cin, S);
	for(t = 0; t < T; t++) {
		getline(cin, S);
		cout<<S.length() - LCS(S, S.length())<<endl;
	}
	return 0;
}