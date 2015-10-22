#include<stdio.h>
#include<iostream>

using namespace std;

int max(int A[], int l, int r) {
	int m = A[l];
	int i;
	for(i = l; i < r; i++) {
		if(m <= A[i]) {
			m = A[i];
		}
	}
	return m;
}

int index(int A[], int l, int r, int maxx) {
	int i;
	for(i = l; i < r; i++) {
		if(A[i] == maxx) {
			return i;
		}
	}
	return -1;
}

int main() {
	int n, k, i;
	cin>>n;
	int A[n];
	for(i = 0 ; i < n; i++) {
		cin>>A[i];
	}
	cin>>k;
	int maxx = max(A, 0, k);
	int ind = index(A, 0, k, maxx);
	cout<<maxx<<" ";
	for(i = 1; i < n-k+1; i++) {
		if(ind == i-1) {
			maxx = max(A, i, i+k);
			ind = index(A, i, i+k, maxx);
		}
		if(A[i+k-1] >= maxx) {
			maxx = A[i+k-1];
			ind = i+k-1;
		}
		cout<<maxx<<" ";
	}
	return 0;
}