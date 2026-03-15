import sys
import heapq

n = int(input())
min_heap = []

for _ in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    for x in row:
        heapq.heappush(min_heap, x)
        if len(min_heap) > n:
            heapq.heappop(min_heap)

print(heapq.heappop(min_heap))