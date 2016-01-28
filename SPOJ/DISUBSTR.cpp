#include<stdio.h>
#include<iostream>
#include<map>
#include<algorithm>
using namespace std;

int LCP(string a, string b) {
  int i;
  for(i = 0; i < min(a.length(), b.length()); i++) {
    if(a[i] != b[i]) {
      return i;
    }
  }
  return i;
}

int main() {
  int T, t, i, j, n, ans;
  string s;
  string suffix_array[50001];
  scanf("%d", &T);
  for(t = 0; t < T; t++) {
    cin>>s;
    n = s.length();
    for(i = 0; i < n; i++) {
      suffix_array[i] = s.substr(i, n);
    }
    sort(suffix_array, suffix_array+n);
    ans = suffix_array[0].length();
    for(i = 0; i < n-1; i++) {
      ans += suffix_array[i+1].length() - LCP(suffix_array[i], suffix_array[i+1]);
    }
    printf("%d\n", ans);
  }
  return 0;
}
