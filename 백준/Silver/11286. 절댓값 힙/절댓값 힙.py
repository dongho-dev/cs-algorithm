import heapq
import sys

data = sys.stdin.read().split()

N = int(data[0])
oper = list(map(int, data[1:]))

abs_heap = []

for x in oper:
    if x != 0:
        heapq.heappush(abs_heap, (abs(x), x))
    elif x == 0:
        if abs_heap:
            print(heapq.heappop(abs_heap)[1])
        else:
            print(0)