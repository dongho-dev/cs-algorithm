import sys
import heapq

# 입력 처리
N, M = map(int, sys.stdin.readline().strip().split())
gift = list(map(int, sys.stdin.readline().strip().split()))
child = list(map(int, sys.stdin.readline().strip().split()))

# 선물 지급 처리
sad = False
gift = [-abs(x) for x in gift]
heapq.heapify(gift)
for i in child:
    giftCount = -heapq.heappop(gift)
    if i > giftCount:
        sad = True
        break
    else:
        temp = -(giftCount - i)
        heapq.heappush(gift, temp) 

# 출력 처리
if sad:
    print(0)
else:
    print(1)