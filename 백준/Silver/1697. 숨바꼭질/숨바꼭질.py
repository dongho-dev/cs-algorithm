import sys
from collections import deque

move = [1, -1]
tp = [2]

n, k = map(int, sys.stdin.readline().strip().split())
dist = [-1] * 100001
q = deque()

dist[n] = 0
q.append(n)

while q:
    cur = q.popleft()
    if cur == k:
        print(dist[cur])
        exit()
    for i in range(3):
        if i == 2:
            nx = cur * tp[0]
        else:
            nx = cur + move[i]
            
        if nx < 0 or nx > 100000:
            continue
        if dist[nx] >= 0:
            continue
        dist[nx] = dist[cur] + 1
        q.append(nx)
