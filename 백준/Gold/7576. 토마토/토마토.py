import sys
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

m, n = map(int, sys.stdin.readline().strip().split())
graph = []
dist = [[-1] * m for _ in range(n)]

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().strip().split())))

q = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            dist[i][j] = 0
            q.append((i, j))

while q:
    cur = q.popleft()
    for x in range(4):
        nx = cur[0] + dx[x]
        ny = cur[1] + dy[x]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if dist[nx][ny] >= 0:
            continue
        if graph[nx][ny] == -1:
            continue
        dist[nx][ny] = dist[cur[0]][cur[1]] + 1
        q.append((nx, ny))

ans = 0

for i in range(n):
    for j in range(m):
        if dist[i][j] == -1 and graph[i][j] == 0:
            print(-1)
            exit()
        ans = max(ans, dist[i][j])

print(ans)