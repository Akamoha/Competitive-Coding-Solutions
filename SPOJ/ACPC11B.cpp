#include<stdio.h>
#include<iostream>

using namespace std;

long long int abs(int x) {
	if(x < 0) {
		return -1*x;
	}
	return x;
}
int main() {
	long long int T, t, N, M, i, j, x, mini, flag, A[1001], B[1001];
	cin>>T;
	for(t = 0; t < T; t++) {
		scanf("%lld", &N);
		for(i = 0; i < N; i++) {
			scanf("%lld", &A[i]);
		}
		scanf("%lld", &M);
		for(j = 0; j < M; j++) {
			scanf("%lld", &B[j]);
		}
		mini = 1000001;
		for(i = 0; i < N; i++) {
			flag = 0;
			for(j = 0; j < M; j++) {
				x = abs(A[i]-B[j]);
				if(x < mini) {
					mini = x;
					if(mini == 0) {
						cout<<0<<endl;
						flag = 1;
						break;
					}
				}
			}
			if(flag) {
				break;
			}
		}
		if(!flag) {
			cout<<mini<<endl;
		}
	}
	return 0;
}