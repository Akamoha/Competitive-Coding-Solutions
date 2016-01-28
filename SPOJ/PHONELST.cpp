#include<stdio.h>
#include<iostream>

using namespace std;

struct node {
  bool is_end;
  struct node* child[10];
} *head;

void init() {
  head = new node();
  head->is_end = false;
  int i;
  for(i = 0; i < 10; i++) {
    head->child[i] = NULL;
  }
}

int main() {
  int T, t, n, i, j;
  bool flag;
  string s;
  scanf("%d", &T);
  for(t = 0; t < T; t++) {
    scanf("%d", &n);
    init();
    flag = true;
    for(i = 0; i < n; i++) {
      cin>>s;
      node* current = head;
      for(j = 0; j < s.length(); j++) {
        if(current->is_end == true) {
          flag = false;
        }
        int letter = (int)(s[j] - (int)'0');
        if(current->child[letter] == NULL) {
          current->child[letter] = new node();
        } else if(j == s.length() - 1) {
          flag = false;
        }
        current = current->child[letter];
      }
      current->is_end = true;
    }
    if(flag  == true) {
      printf("YES\n");
    } else {
      printf("NO\n");
    }
  }
}
