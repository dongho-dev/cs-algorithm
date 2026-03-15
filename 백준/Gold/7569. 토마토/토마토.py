from collections import deque
import sys

dx = [0, 1, 0, -1, 0, 0]
dy = [1, 0, -1, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs():
    while q:
        z, y, x = q.popleft()
        for t in range(6):
            nx = x + dx[t]
            ny = y + dy[t]
            nz = z + dz[t]
            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H:
                if zone[nz][ny][nx] == 0 and day[nz][ny][nx] == -1:
                    day[nz][ny][nx] = day[z][y][x] + 1
                    q.append((nz, ny, nx))

M, N, H = map(int, input().split()) # M: 가로, N: 세로, H: 층 수

day = [[[-1] * M for _ in range(N)] for _ in range(H)] # 날짜 맵 -1로 초기화
zone = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

# BFS를 위한 큐 초기화
q = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if zone[i][j][k] == 1:
                q.append((i, j, k))
                day[i][j][k] = 0

# BFS 수행
bfs()

# 결과 확인
resultD = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if zone[i][j][k] == 0 and day[i][j][k] == -1:
                print("-1")
                sys.exit()
            resultD = max(resultD, day[i][j][k])

print(resultD)
