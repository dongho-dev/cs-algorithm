import sys
from collections import deque

move = [1, -1]
tp = [2]

n, k = map(int, sys.stdin.readline().strip().split())
dist = [-1] * 100001
count = [0] * 100001
q = deque()

dist[n] = 0
count[n] = 1
q.append(n)

while q:
    cur = q.popleft()
    if cur == k:
        print(dist[cur])
        print(count[cur])
    for i in range(3):
        if i == 2:
            nx = cur * tp[0]
        else:
            nx = cur + move[i]
            
        if nx < 0 or nx > 100000:
            continue
        if dist[nx] >= 0:
            if dist[nx] == dist[cur] + 1:
                count[nx] += count[cur]
            continue
        dist[nx] = dist[cur] + 1
        count[nx] = count[cur]
        q.append(nx)
        

