#include<stdio.h>
#include<iostream>

#define MAX 1000001

using namespace std;

void solve(char DP[], int current, int x, int K, int L) {
	int i;
	for(i = current + 1; i <= x; i++) {
		if(DP[i - 1] == 'A') {
			if(i - K > 0 && DP[i - K] == 'A') {
				if(i - L > 0 && DP[i - L] == 'A') {
					DP[i] = 'B';
					continue;
				} else if(i - L < 0) {
					DP[i] = 'B';
					continue;
				}
			} else if(i - K < 0) {
				DP[i] = 'B';
				continue;
			}
		}
		DP[i] = 'A';
	}
}

int main() {
	int K, L, m, i, x, current;
	char DP[MAX];
	scanf("%d %d %d", &K, &L, &m);
	for(i = 1; i < MAX; i++) {
		DP[i] = 'C';
	}
	DP[1] = 'A';
	current = 1;
	for(i = 0; i < m; i++) {
		scanf("%d", &x);
		if(DP[x] == 'C') {
			solve(DP, current, x, K, L);
		}
		cout<<DP[x];
		current = x;
	}
	return 0;
}