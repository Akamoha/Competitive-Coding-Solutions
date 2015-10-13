#include<stdio.h>
#include<iostream>

#define MAX 102

using namespace std;

int max(int a, int b, int c) {
	if(a > b) {
		if(a > c) {
			return a;
		}
		return c;
	}
	if(b > c) {
		return b;
	}
	return c;
}

int max(int arr[], int size) {
	int it, maxval = 0;
	for(it = 0; it < size; it++) {
		if(maxval < arr[it]) {
			maxval = arr[it];
		}
	}
	return maxval;
}

int main() {
	int T, i, j, t, h, w, tiles[MAX][MAX], DP[MAX][MAX];
	cin>>T;
	for(t = 0; t < T; t++) {
		cin>>h>>w;
		for(i = 0; i < h; i++) {
			for(j = 0; j < w; j++) {
				cin>>tiles[i][j];
				DP[i][j] = 0;
			}
			DP[i][w] = 0;
			DP[i][w+1] = 0;
		}
		
		for(j = 0; j < w; j++) {
			DP[0][j+1] = tiles[0][j];
		}
		
		for(i = 1; i < h; i++) {
			for(j = 1; j < w + 1; j++) {
				DP[i][j] = tiles[i][j-1] + max(DP[i-1][j-1], DP[i-1][j], DP[i-1][j+1]);
			} 
		}
		
		cout<<max(DP[h-1], w+2)<<endl;
	}
	return 0;
}