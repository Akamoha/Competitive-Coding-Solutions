#include<stdio.h>
#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int L[2001];

int compare (const void * a, const void * b) { return ( *(int*)a - *(int*)b ); }

int binSearch(int begin, int end, int key) {
  int mid, x, it;
  if(begin < end) {
    mid = (begin+end)/2;
    if(key < L[mid]) {
      return binSearch(begin, mid, key);
    } else if(key > L[mid]) {
      return binSearch(mid+1, end, key);
    } else {
      for(it = mid+1; it < end; it++) {
        if(L[it] > L[mid]) {
          break;
        }
      }
      return it;
    }
  }
  return (begin+end)/2;
}

int main() {
  int N, i, j, count;
  while(1) {
    scanf("%d", &N);
    if(N == 0) {
      break;
    }
    for(i = 0; i < N; i++) {
      scanf("%d", &L[i]);
    }
    qsort(L, N, sizeof(int), compare);
    count = 0;
    for(i = 0; i < N-2; i++) {
      for(j = i+1; j < N-1; j++) {
        count += N - binSearch(j+1, N, L[i]+L[j]);
      }
    }
    printf("%d\n", count);
  }
  return 0;
}
