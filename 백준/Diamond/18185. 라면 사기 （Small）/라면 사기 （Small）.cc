// 0.5 초 (추가 시간 없음)	32 MB
#include <stdio.h>
#ifndef min
#define min(a,b)  (((a) < (b)) ? (a) : (b))
#endif
int main(void) {
	int N; //  라면 공장의 개수, 3 ≤ N ≤ 10^4
	int A[11111]; // 0 ≤ Ai ≤ 10^4 (1 ≤ i ≤ N)
	int small = 0; // 최소 비용
	scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		scanf("%d", &A[i]);
	}
	
	for (int i = 0; i < N; i++) {
		if (A[i + 1] > A[i + 2]) {
			int a = min(A[i], A[i + 1] - A[i + 2]);
			small += a * 5;
			A[i] -= a;
			A[i + 1] -= a;
		
			int b1 = min(A[i], A[i + 1]);
			int b2 = min(A[i + 1], A[i + 2]);
			int b3 = min(b1, b2);
			small += b3 * 7;
			A[i] -= b3;
			A[i + 1] -= b3;
			A[i + 2] -= b3;
	    } else {
			int b1 = min(A[i], A[i + 1]);
			int b2 = min(A[i + 1], A[i + 2]);
			int b3 = min(b1, b2);
			small += b3 * 7;
			A[i] -= b3;
			A[i + 1] -= b3;
			A[i + 2] -= b3;
			
			int a = min(A[i], A[i + 1]);
			small += a * 5;
			A[i] -= a;
			A[i + 1] -= a;
		}
		
		small += A[i] * 3;
	}
	
	
	printf("%d", small);
}

