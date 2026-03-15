import sys
import heapq

# 입력 처리
N = int(sys.stdin.readline().strip())

# 중간값 계산 후 출력 처리
leftHeap = []
rightHeap = []

for _ in range(N):
    n = int(sys.stdin.readline().strip())
    if not leftHeap or n <= -leftHeap[0]:
        heapq.heappush(leftHeap, -n)
    else:
        heapq.heappush(rightHeap, n)

    if len(leftHeap) < len(rightHeap):
        heapq.heappush(leftHeap, -heapq.heappop(rightHeap))
    elif len(leftHeap) - len(rightHeap) > 1:
        heapq.heappush(rightHeap, -heapq.heappop(leftHeap))

    median = -leftHeap[0]
    print(median)
