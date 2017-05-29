#include <iostream>
#include <algorithm>
#include <vector>
#include <utility>
using namespace std;
 
 
 
struct sortKey
{
    inline bool operator() (const pair<int, int>& struct1, const pair<int, int>& struct2)
    {
    	if(struct1.first != struct2.first)
        	return struct1.first < struct2.first;
        else
        	return struct1.second > struct2.second;
    }
};
 
 
// The snakes are trimmed accordingly
int getSolution(int startIndex, int endIndex, vector<pair<int, int> > snakes) {
	if(snakes.size() == 0)
		return -1;
	if(snakes.size() == 1 && (snakes[0].first != startIndex || snakes[0].second != endIndex))
		return -1;
	if(snakes.size() == 1 && snakes[0].first == startIndex && snakes[0].second == endIndex)
		return 1;
 
	sort(snakes.begin(), snakes.end(), sortKey());
	
	// cerr << "startIndex: " << startIndex << " endIndex: " << endIndex << endl;
	// for(int i=0; i<snakes.size(); i++)
	// 	cerr << "(" << snakes[i].first << ", " << snakes[i].second << ") ";
	// cerr << endl;
 
	// Pick the first snake
	int currStart = snakes[0].first;
	int currEnd = snakes[0].second;
	int currSnake = 0;
	int count = 0;
 
	int i=1;
	while(i<snakes.size()) {
		count++;
		int nextSnakeToPick = -1;
		for(; i<snakes.size(); i++) {
 
			// No more snakes left overlapping with currSnake
			if(snakes[i].first > currEnd+1) {
				// Did not decide the next snake as all connected snakes (if any) after currSnake were completely overshadowed by currSnake
				if(nextSnakeToPick == -1)
					return -1;
				break;
			}
			// This snakes starting portion has connected to the currSnake
			else {
				// Found a better next snake
				if(nextSnakeToPick != -1 && snakes[nextSnakeToPick].second < snakes[i].second)
					nextSnakeToPick = i;
				// Found the first snake not completely overlapping with current snake
				else if (snakes[i].second > currEnd)
					nextSnakeToPick = i;
			}
		}
		// cerr << "Chose " << nextSnakeToPick << " after " << currSnake  << endl;
 
		// Snaked finished
		if(i == snakes.size()) {
			if(nextSnakeToPick != -1) {
				if(snakes[nextSnakeToPick].second == endIndex)
					return count + 1;
				else
					return -1;
			} else if(nextSnakeToPick == -1) {
				if(currEnd == endIndex)
					return count;
				else
					return -1;
			}
		}
		else {
			currSnake = nextSnakeToPick;
			currEnd = snakes[currSnake].second;
			currStart = snakes[currSnake].first;
		}
	}
	return -1;
}
 
 
int main () {
	int cases;
	cin >> cases;
	while(cases--) {
		int n, k, numberOfSnakes;
		cin >> n >> k >> numberOfSnakes;
 
		int startIndex = (n-k)/2 + 1;
		int endIndex = startIndex + k - 1;
 
		vector<pair<int, int> > horizontalProtectors;
		vector<pair<int, int> > verticalProtectors;
		while(numberOfSnakes--) {
			int hx, hy, tx, ty;
			cin >> hx >> hy >> tx >> ty;
 
			// Horizontal snake
			if(hx == tx) {
				if(hx >= startIndex && hx <= endIndex) {
					//cerr << "Adding vertical protector (" << hx << ", " << hx << ") for snake " << hx << " " << hy << " " << tx << " " << ty << endl; 
					verticalProtectors.push_back(make_pair(hx, hx));
				}
				else {
					int head = min(hy, ty);
					int tail = max(hy, ty);
					// Check if this snake protects the prison or not
					if(tail>=startIndex && head<=endIndex) {
						horizontalProtectors.push_back(make_pair(max(head, startIndex), min(tail, endIndex)));
						//cerr << "Adding horizontal protector (" << max(head, startIndex) << ", " << min(tail, endIndex) << ") for snake " << hx << " " << hy << " " << tx << " " << ty << endl; 
					}
				}
			}
			// Vertical snake 
			else if(hy == ty) {
				if(hy >= startIndex && hy <= endIndex) {
					//cerr << "Adding horizontal protector (" << hy << ", " << hy << ") for snake " << hx << " " << hy << " " << tx << " " << ty << endl; 
					horizontalProtectors.push_back(make_pair(hy, hy));
				}
				else {
					int head = min(hx, tx);
					int tail = max(hx, tx);
					// Check if this snake protects the prison or not
					if(tail>=startIndex && head<=endIndex) {
						verticalProtectors.push_back(make_pair(max(head, startIndex), min(tail, endIndex)));
						//cerr << "Adding vertical protector (" << max(head, startIndex) << ", " << min(tail, endIndex) << ") for snake " << hx << " " << hy << " " << tx << " " << ty << endl; 
					}
 
				}
			}
		}
 
		int horizontalSnakeCounts = getSolution(startIndex, endIndex, horizontalProtectors);
		//cout << "got " << horizontalSnakeCounts << endl;
		int verticalSnakeCounts = getSolution(startIndex, endIndex, verticalProtectors);
		//cout << "got " << verticalSnakeCounts << endl;
 
		if(horizontalSnakeCounts != -1 && verticalSnakeCounts != -1)
			cout << horizontalSnakeCounts + verticalSnakeCounts << endl;
		else
			cout << -1 << endl;
	}
	return 0;
}