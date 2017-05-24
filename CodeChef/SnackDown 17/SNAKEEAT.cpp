#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
 
class greater
{
public:
    template<class T>
    bool operator()(T const &a, T const &b) const { return a > b; }
};
 
 
long long binSearch(const vector <long long> & snakeLengths, long long key) {
	long long start = 0;
	long long end = snakeLengths.size() -1;
 
	while(start <= end) {
		if(start + 1 == end) {
			if(snakeLengths[end] >= key)
				return end;
			else if(snakeLengths[start] >= key)
				return start;
			else
				return -1;
		}
		else if(start == end) {
			if(snakeLengths[start] >= key)
				return start;
			else
				return -1;
		}
		else {
			long long mid = (start + end)/2;
			if(snakeLengths[mid] >= key)
				start = mid;
			else
				end = mid - 1;
		}
	}
	return -1;
}
 
 
long long getSolution (const vector<long long> & snakeLengths, const vector<long long> & cumulativeScore, long long minLength) {
	// This will never arise
	if(snakeLengths.size() == 0)
		return 0;
 
	// maxIndex is the index of the last element in snakeLengths that is >= minLength
	long long maxIndex = binSearch(snakeLengths, minLength);
	if(maxIndex == snakeLengths.size() -1)
		return snakeLengths.size();
 
	long long start = 0;
	long long end = snakeLengths.size() - 1;
	long long extraCumulativeSum = 0;
	long long count = 0;
 
	if(maxIndex != -1) {
		start = maxIndex + 1;
		extraCumulativeSum = cumulativeScore[maxIndex];
		count = maxIndex + 1;
	}
 
 
	long long mid;
	while(start <= end) {
		if(start + 1 == end) {
			if(minLength*(end - maxIndex) - (cumulativeScore[end] - extraCumulativeSum) <= snakeLengths.size() - end - 1)
				return end + 1;
			else if (minLength*(start - maxIndex) - (cumulativeScore[start] - extraCumulativeSum) <= snakeLengths.size() - start - 1)
				return start + 1;
			else
				return count;
		} else if(start == end) {
			if(minLength*(end - maxIndex) - (cumulativeScore[end] - extraCumulativeSum) <= snakeLengths.size() - end - 1)
				return end + 1;
			else
				return count;
		}
		else {
			mid = (start + end)/2;
			if(minLength*(mid - maxIndex) - (cumulativeScore[mid] - extraCumulativeSum) <= snakeLengths.size() - mid - 1)
				start = mid;
			else
				end = mid - 1;
		}
	}
 
	return 100000;
}
 
 
int main () {
	int cases;
	cin >> cases;
	while(cases --) {
		int n, q;
		cin >> n >> q;
 
		// Read original snakeLengths
		vector<long long> snakeLengths(n);
		for(int i=0; i<n; i++) {
			cin >> snakeLengths[i];
		}
		sort(snakeLengths.rbegin(), snakeLengths.rend());   // note: reverse iterators
		
		// Calculate cumulative score
		vector<long long> cumulativeScore(n);
		long long tempCumulativeScore = 0;
		for(int i=0; i<snakeLengths.size(); i++){
			tempCumulativeScore += snakeLengths[i];
			cumulativeScore[i] = tempCumulativeScore;
		}
 
		// Treat all test cases independently
		while(q--) {
			long long minLength;
			cin >> minLength;
			cout << getSolution(snakeLengths, cumulativeScore, minLength) << endl;
		}
	}
	return 0;
} 