import heapq
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
oper = list(map(int, data[1:]))

min_heap = []

for x in oper:
    if x > 0:
        heapq.heappush(min_heap, x)
    elif x == 0:
        if min_heap:
            print(heapq.heappop(min_heap))
        else:
            print(0)

