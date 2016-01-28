#include<stdio.h>
#include<iostream>
#include<map>

using namespace std;

int main() {
  int n1, n2, i, ans, prevhit;
  int seq1[10001], seq2[10001], csa1[10001], csa2[10001];
  map<int, int> HT;
  scanf("%d", &n1);
  while(n1 != 0) {
    scanf("%d", &seq1[0]);
    HT.clear();
    csa1[0] = seq1[0];
    for(i = 1; i < n1; i++) {
      scanf("%d", &seq1[i]);
      csa1[i] = seq1[i] + csa1[i-1];
    }
    seq1[n1] = 1000001;
    csa1[n1] = csa1[n1-1];
    scanf("%d", &n2);
    scanf("%d", &seq2[0]);
    csa2[0] = seq2[0];
    HT[seq2[0]] = 0;
    for(i = 1; i < n2; i++) {
      scanf("%d", &seq2[i]);
      csa2[i] = seq2[i] + csa2[i-1];
      HT[seq2[i]] = i;
    }
    seq2[n2] = 1000001;
    csa2[n2] = csa2[n2-1];
    HT[seq2[n2]] = n2;
    ans = 0;
    prevhit = -1;
    int x;
    for(i = 0; i < n1+1; i++) {
      if(HT.count(seq1[i]) != 0) {
        if(prevhit == -1) {
          x = max(csa1[i], csa2[HT[seq1[i]]]);
        } else {
          x = max(csa1[i]-csa1[prevhit], csa2[HT[seq1[i]]]-csa2[HT[seq1[prevhit]]]);
        }
        ans += x;
        prevhit = i;
      }
    }
    printf("%d\n", ans);
    scanf("%d", &n1);
  }
  return 0;
}
