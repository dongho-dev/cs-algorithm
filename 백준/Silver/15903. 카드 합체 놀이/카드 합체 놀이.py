import sys
import heapq

# 입력 처리
n, m = map(int, sys.stdin.readline().strip().split())
card = list(map(int, sys.stdin.readline().strip().split()))

# 합체 처리
heapq.heapify(card)

for _ in range(m):
    first = heapq.heappop(card)
    second = heapq.heappop(card)
    combine = first + second
    heapq.heappush(card, combine)
    heapq.heappush(card, combine)

# 출력 처리
print(sum(card))