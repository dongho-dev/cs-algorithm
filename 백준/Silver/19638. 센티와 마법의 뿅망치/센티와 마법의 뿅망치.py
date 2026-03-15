import sys
import heapq

# 입력 처리
N, H, T = map(int, sys.stdin.readline().strip().split())
heightHeap = []

for _ in range(N):
    height = int(sys.stdin.readline().strip())
    heapq.heappush(heightHeap, -height)

# 뿅망치 처리
minimumCount = 0

for i in range(T):
    top = -heightHeap[0]
    if top < H:
        minimumCount = i
        break
    
    target = -heapq.heappop(heightHeap)
    if target == 1:
        heapq.heappush(heightHeap, -target)
        minimumCount = i + 1
        break
        
    target = target // 2
    heapq.heappush(heightHeap, -target)
else:
    minimumCount = T

# 출력 처리
top = -heightHeap[0]
if H > top:
    print("YES")
    print(minimumCount)
else:
    print("NO")
    print(top)