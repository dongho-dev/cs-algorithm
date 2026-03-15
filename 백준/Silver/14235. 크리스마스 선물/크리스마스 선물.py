import sys
import heapq

# 입력 처리
N = int(sys.stdin.readline().strip())

# 선물 처리 및 출력 처리
maxHeap = []

for _ in range(N):
    A = list(map(int, sys.stdin.readline().strip().split()))
    if not A[0] == 0:
        del A[0]
        for i in A:
            heapq.heappush(maxHeap, -i)
    else:
        if maxHeap:
            print(-heapq.heappop(maxHeap))
        else:
            print(-1)
