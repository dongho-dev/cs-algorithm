import sys
import heapq

N = int(sys.stdin.readline().strip())

minHeap = []
minHeapEnd =[]

for _ in range(N):
    S, T = map(int, sys.stdin.readline().strip().split())
    heapq.heappush(minHeap, (S, T))

while minHeap:
    A = minHeap[0][0]
    B = minHeap[0][1]
    if minHeapEnd:
        if A >= minHeapEnd[0]:
            heapq.heappop(minHeapEnd)
    
    heapq.heappush(minHeapEnd, B)
    heapq.heappop(minHeap)

print(len(minHeapEnd))
