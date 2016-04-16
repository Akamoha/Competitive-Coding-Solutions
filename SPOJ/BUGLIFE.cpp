#include<stdio.h>
#include<iostream>
#include<bits/stdc++.h>

#define sd(x) scanf("%d", &x);

using namespace std;

vector<vector<int> > g;
vector<int> visited;

bool DFS(int s, int p, int color) {
  visited[s] = color;
  for(int i = 0; i < g[s].size(); i++) {
    if(g[s][i] != p) {
      if(visited[g[s][i]] == visited[s]) {
        return false;
      }
    }
  }
  for(int i = 0; i < g[s].size(); i++) {
    if(g[s][i] != p) {
      if(visited[g[s][i]] == -1) {
        if(!DFS(g[s][i], s, 1-color)) {
          return false;
        }
      }
    }
  }
  return true;
}

int main() {
  int T, t, i, N, M, u, v;
  sd(T);
  for(t = 0; t < T; t++) {
    printf("Scenario #%d:\n", t+1);
    sd(N); sd(M);
    g.clear();
    for(i = 0; i <= N; i++) {
      vector<int> empty;
      g.push_back(empty);
    }
    for(i = 0; i < M; i++) {
      sd(u); sd(v);
      g[u].push_back(v);
      g[v].push_back(u);
    }
    visited.clear();
    for(i = 0; i <= N; i++) {
      visited.push_back(-1);
    }
    bool flag = false;
    for(i = 1; i <= N; i++) {
      if(visited[i] == -1) {
        if(!DFS(i, 0, 1)) {
          printf("Suspicious bugs found!\n");
          flag = true;
          break;
        }
      }
    }
    if(!flag) {
      printf("No suspicious bugs found!\n");
    }
  }
}
