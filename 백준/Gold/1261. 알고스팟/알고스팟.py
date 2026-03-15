from collections import deque

def minWallsBreak(N, M, map):
  directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

  dist = [[float('INF')] * M for _ in range(N)]
  dist[0][0] = 0

  q = deque([(0, 0)])
  while q:
    x, y = q.popleft()
    for dx, dy in directions:
      nx, ny = x + dx, y + dy
      if 0 <= nx < N and 0 <= ny < M:
        if map[nx][ny] == 0 and dist[nx][ny] > dist[x][y]:
          dist[nx][ny] = dist[x][y]
          q.appendleft((nx, ny))
        elif map[nx][ny] == 1 and dist[nx][ny] > dist[x][y] + 1:
          dist[nx][ny] = dist[x][y] + 1
          q.append((nx, ny))
  return dist[N-1][M-1]

M, N = map(int, input().split())
map = [list(map(int, input().strip())) for _ in range(N)]
print(minWallsBreak(N, M, map))