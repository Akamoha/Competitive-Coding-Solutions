#include <iostream>
#include <vector>
#include <climits>
using namespace std;
 
void getCumulativeArray(const vector<long long> & initialHeights, vector<long long> & cumulativeLR, vector<long long> & cumulativeRL);
void getMaximumPossiblHeights(const vector<long long> & initialHeights, vector<long long> & maxHeightsLR, vector<long long> & maxHeightsRL);
long long getSolution(const vector<long long> & initialHeights);
 
void getCumulativeArray(const vector<long long> & initialHeights, vector<long long> & cumulativeLR, vector<long long> & cumulativeRL) {
	cumulativeLR[0] = initialHeights[0];
	for(long long i=1; i<initialHeights.size(); i++)
		cumulativeLR[i] = cumulativeLR[i-1] + initialHeights[i];
 
	cumulativeRL[initialHeights.size()-1] = initialHeights[initialHeights.size()-1];
	for(long long i=initialHeights.size()-2; i>=0; i--)
		cumulativeRL[i] = cumulativeRL[i+1] + initialHeights[i];
}
 
void getMaximumPossiblHeights(const vector<long long> & initialHeights, vector<long long> & maxHeightsLR, vector<long long> & maxHeightsRL) {
	maxHeightsLR[0] = 1;
	for(long long i=1; i<initialHeights.size(); i++)
		maxHeightsLR[i] = min(initialHeights[i], maxHeightsLR[i-1]+1);
 
	maxHeightsRL[initialHeights.size()-1] = 1;
	for(long long i=initialHeights.size()-2; i>=0; i--)
		maxHeightsRL[i] = min(initialHeights[i], maxHeightsRL[i+1]+1);
}
 
// Assume all initialHeights[i] >= 1
// Assume initialHeights.size() >= 1
long long getSolution(const vector<long long> & initialHeights) {
 
	// Get maximum possible heights from both directions
	vector<long long> maxHeightsLR (initialHeights.size());
	vector<long long> maxHeightsRL (initialHeights.size());
	getMaximumPossiblHeights(initialHeights, maxHeightsLR, maxHeightsRL);
 
	// Get cumulative arrays [for final cost calculation in O(1)] from both directions
	vector<long long> cumulativeLR (initialHeights.size());
	vector<long long> cumulativeRL (initialHeights.size());
	getCumulativeArray(initialHeights, cumulativeLR, cumulativeRL);
 
	// Debug
	// for(int i=0; i<initialHeights.size(); i++)
	// 	cout << maxHeightsLR[i] << " ";
	// cout << endl;
	// for(int i=0; i<initialHeights.size(); i++)
	// 	cout << maxHeightsRL[i] << " ";
	// cout << endl;
	// for(int i=0; i<initialHeights.size(); i++)
	// 	cout << cumulativeLR[i] << " ";
	// cout << endl;
	// for(int i=0; i<initialHeights.size(); i++)
	// 	cout << cumulativeRL[i] << " ";
	// cout << endl;
	
	// Get minimum cost
	long long minCost = LLONG_MAX;
	for(long long i=0; i<initialHeights.size(); i++) {
		long long maxHeightOftemple = min(maxHeightsLR[i], maxHeightsRL[i]);
		long long totalBlocksOnL = ((maxHeightOftemple)*(maxHeightOftemple+1))/2 /*+ (i - maxHeightOftemple + 1)*/;
		long long totalBlocksOnR = ((maxHeightOftemple)*(maxHeightOftemple+1))/2 /*+ (initialHeights.size() - (i + maxHeightOftemple))*/;
		long long cost = (cumulativeLR[i] - totalBlocksOnL) + (cumulativeRL[i] - totalBlocksOnR) - (initialHeights[i] - maxHeightOftemple);
		minCost = min(minCost, cost);
	}
	return minCost;
}
 
 
int main() {
	long long cases;
	cin >> cases;
	while(cases--) {
		long long n;
		cin >> n;
		vector<long long> initialHeights(n);
		for(long long i=0; i<n; i++)
			cin >> initialHeights[i];
		cout << getSolution(initialHeights) << endl;
	}
	return 0;
}