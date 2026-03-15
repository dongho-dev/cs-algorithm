from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(i, j, k):
  q = deque()
  q.append((i, j))
  while q:
    x, y = q.popleft()
    visit[x][y] = True
    for i in range(4): # 시작 좌표부터 상하좌우로 탐색
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= N or ny < 0 or ny >= N: # 맵 밖으로 나가면 넘어감
        continue
      if visit[nx][ny] == True: # 이미 방문했다면 넘어감
        continue
      if k != zone[nx][ny]: # 다른 색이라면 넘어감
        continue
      visit[nx][ny] = True # 방문 처리하고 큐에 넣음
      q.append((nx, ny))      

def bbfs(i, j, k):
  q = deque()
  q.append((i, j))
  while q:
    x, y = q.popleft()
    visit[x][y] = True
    for i in range(4): # 시작 좌표부터 상하좌우로 탐색
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= N or ny < 0 or ny >= N: # 맵 밖으로 나가면 넘어감
        continue
      if visit[nx][ny] == True: # 이미 방문했다면 넘어감
        continue
      if k == 3: # 파란색이라면 다른 색인 경우 넘어감
        if zone[nx][ny] != 3:
          continue
      else: # 초록, 빨간색이라면 파란색인 경우 넘어감
        if zone[nx][ny] == 3:
          continue
      visit[nx][ny] = True # 방문 처리하고 큐에 넣음
      q.append((nx, ny))     
        
N = int(input()) # 맵 크기
visit = [[False] * N for _ in range(N)] # False로 방문 맵 초기화
zone = [[0] * N for _ in range(N)] # 0으로 그리드 맵 초기화
j = 0
for i in range(N):
  s = input().strip()
  for j in range(N):    
    if s[j] == 'R':
      zone[i][j] = 1
    elif s[j] == 'G':
      zone[i][j] = 2
    elif s[j] == 'B':
      zone[i][j] = 3
  

# 모든 좌표에 대해서 영역 확인
zoneNum = 0
for i in range(N):
  for j in range(N):
    if visit[i][j] == True: # 방문했었다면 넘어감
      continue
    bfs(i, j, zone[i][j])
    zoneNum += 1

visit = [[False] * N for _ in range(N)] # False로 방문 맵 초기화
bzoneNum = 0
for i in range(N):
  for j in range(N):
    if visit[i][j] == True: # 방문했었다면 넘어감
      continue
    bbfs(i, j, zone[i][j])   
    bzoneNum += 1

print(zoneNum, bzoneNum)