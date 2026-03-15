import sys
import heapq

# 입력 처리
T = int(sys.stdin.readline().strip())
for _ in range(T):
    minQ = []
    maxQ = []

    K = int(sys.stdin.readline().strip())
    visited = [False] * K

    for i in range(K):
        S, N = sys.stdin.readline().strip().split()
        N = int(N)

        if S == 'I':
            heapq.heappush(minQ, (N, i))
            heapq.heappush(maxQ, (-N, i))
            visited[i] = True
        elif S == 'D':
            if N == 1:
                while maxQ and not visited[maxQ[0][1]]:
                    heapq.heappop(maxQ)
                if maxQ:
                    _, idx = heapq.heappop(maxQ)
                    visited[idx] = False
            elif N == -1: 
                while minQ and not visited[minQ[0][1]]:
                    heapq.heappop(minQ)
                if minQ:
                    _, idx = heapq.heappop(minQ)
                    visited[idx] = False
            
    while maxQ and not visited[maxQ[0][1]]:
        heapq.heappop(maxQ)
    while minQ and not visited[minQ[0][1]]:
        heapq.heappop(minQ)

    if not minQ or not maxQ:
        print("EMPTY")
    else:
        minimum = minQ[0][0]
        maximum = -maxQ[0][0]
        print(maximum, minimum)

