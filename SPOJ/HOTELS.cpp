#include<stdio.h>
#include<iostream>

using namespace std;

int main() {
	int N, M, i, j, max = 0, sum = 0;
	cin>>N>>M;
	int A[N];
	for(i = 0; i < N; i++) {
		cin>>A[i];
	}
	j = 0;
	for(i = 0; j < N;) {
		if(sum + A[j] <= M) {
			sum += A[j];
			j++;
			if(max < sum) {
				max = sum;
			}
		}
		else {
			sum -= A[i];
			i++;
		}
	}
	cout<<max;
	return 0;
}