#include<bits/stdc++.h>

#define sd(x) scanf("%d", &x);
#define slld(x) scanf("%lld", &x);
#define print(x) printf("%lld\n", x);
#define ll long long int
#define TYPE int

using namespace std;

struct node {
	TYPE data;
	node* parent;
	int rank;
};

map<TYPE, node*> MAP;

void makeSet(TYPE data) {
	node* newNode = new node();
	newNode->data = data;
	newNode->parent = newNode;
	newNode->rank = 0;
	MAP[data] = newNode;
}

node* findSet(node* n) {
	node* parent = n->parent;
	if(parent == n) {
		return parent;
	}
	n->parent = findSet(n->parent);
	return n->parent;
}

TYPE findSet(TYPE data) {
	return findSet(MAP[data])->data;
}

bool unionFunc(TYPE data1, TYPE data2) {
	node* n1 = MAP[data1];
	node* n2 = MAP[data2];
	node* parent1 = findSet(n1);
	node* parent2 = findSet(n2);
	
	if(parent1->data == parent2->data) {
		return false;
	}
	if(parent1->rank == parent2->rank) {
		parent1->rank++;
		parent2->parent = parent1;
	} else if(parent1->rank > parent2->rank) {
		parent2->parent = parent1;
	} else {
		parent1->parent = parent2;
	}
	return true;
}

int main() {
	int T, t, N, M, m, n, i, j, k, milkmanornot;
	sd(T);
	vector<pair<int, pair<int, int> > > edges;
	vector<pair<int, pair<int, int> > > MSTedges;
	vector<int> milkman;
	for(t = 0; t < T; t++) {
		sd(N); sd(M);
		MAP.clear();
		edges.clear();
		MSTedges.clear();
		milkman.clear();
		milkman.push_back(1);
		bool somemilkmanthere = true;
		for(n = 1; n <= N; n++) {
			sd(milkmanornot);
			milkman.push_back(milkmanornot);
			if(milkmanornot == 1)
				somemilkmanthere = true;
		}
		if(!somemilkmanthere) {
			printf("impossible\n");
			continue;
		}
		ll answer = 0;
		for(m = 0; m < M; m++) {
			sd(i); sd(j); sd(k);
			edges.push_back(make_pair(k, make_pair(i, j)));
		}
		for(n = 1; n <= N; n++) {
			if(milkman[n] == 1) {
				edges.push_back(make_pair(0, make_pair(n, 0)));
			}
		}
		for(i = 0; i <= N; i++) {
			makeSet(i);
		}
		sort(edges.begin(), edges.end());
		for(i = 0; i < edges.size(); i++) {
			TYPE root1 = findSet(edges[i].second.first);
			TYPE root2 = findSet(edges[i].second.second);
			if(root1 == root2) {
				continue;
			} else {
				int v1 = edges[i].second.first;
				int v2 = edges[i].second.second;
				MSTedges.push_back(edges[i]);
				unionFunc(root1, root2);
				answer += edges[i].first;
			}
		}
		bool impossible = false;
		for(n = 1; n <= N; n++) {
			if(findSet(n) != findSet(0)) {
				printf("impossible\n");
				impossible = true;
				break;
			}
		}
		if(!impossible)
			print(answer);
	}
	return 0;
}