#include <iostream>
#include <algorithm>
#include <stack>

using namespace std;

stack<pair<int, int>> s;
int h[500001]; // 키 저장

int main() {
	long long count = 0; // 쌍의 수
	int same_height = 0; // 같은 키의 사람의 수
	int N;
	cin >> N;  // 줄에서 기다리고 있는 사람의 수 N 입력받기
	
	// 줄에서 기다리고 있는 사람들의 키 입력받기
	for (int i = 0; i < N; i++) {
		cin >> h[i]; 
	}
	
	for (int i = 0; i < N; i++) {
		// 스택의 루트값과 비교. 스택이 비거나 루트값이 크거나 같을때까지 반복.
		while (!s.empty() && s.top().first < h[i]) { 
			count += 1;
			s.pop();
		}
		
		// 스택이 비어있지 않은 경우
		if (!s.empty()) {
			if (s.top().first == h[i]) { // 루트값과 키가 같은 경우
				s.push(make_pair(h[i], s.top().second + 1));
				if (s.size() == s.top().second) {
					count += (s.top().second - 1);
				} else if (s.size() > s.top().second) {
					count += s.top().second;
				}
			} else { // 루트값이 키보다 클 경우
				count += 1;
				s.push(make_pair(h[i], 1));
			}
		} else {
			// 스택이 빈 경우 (스택 내 모든 키보다 더 큰 경우.)
			s.push(make_pair(h[i], 1));
		}
	}
	
	cout << count;
	return 0;
}
