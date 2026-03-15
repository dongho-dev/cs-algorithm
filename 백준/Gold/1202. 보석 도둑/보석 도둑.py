import sys
import heapq

# 입력 처리
N, K = map(int, sys.stdin.readline().split()) # N개의 보석, K개의 가방

crystal = []
C = [] # 가방 용량

for _ in range(N):
    m, v = map(int, sys.stdin.readline().split()) # 무게, 가격
    crystal.append((m, v))

for _ in range(K):
    c = int(sys.stdin.readline())
    C.append(c)

# 최대 가격 구하기
result = 0
C.sort() 
crystal.sort(key=lambda x: (x[0], -x[1]))
maxHeap = []
j = 0

for i in C:
    while j < N and crystal[j][0] <= i:
        heapq.heappush(maxHeap, -crystal[j][1])
        j += 1

    if maxHeap:
        result += -heapq.heappop(maxHeap)

# 출력 처리
print(result)