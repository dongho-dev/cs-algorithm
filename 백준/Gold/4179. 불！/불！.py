import sys
from collections import deque

# 입력의 첫째 줄에는 공백으로 구분된 두 정수 R과 C가 주어진다. 단, 1 ≤ R, C ≤ 1000 이다. R은 미로 행의 개수, C는 열의 개수이다.
# 다음 입력으로 R줄동안 각각의 미로 행이 주어진다.
# 각각의 문자들은 다음을 뜻한다.

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

r, c = map(int, sys.stdin.readline().strip().split())

graph = []
day1 = [[-1] * c for _ in range(r)]
day2 = [[-1] * c for _ in range(r)]

for i in range(r):
    graph.append(list(sys.stdin.readline().strip()))

q1 = deque()
q2 = deque()

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'F':
            day1[i][j] = 0
            q1.append((i, j))

while q1:
    cur = q1.popleft()
    for i in range(4):
        nx = cur[0] + dx[i]
        ny = cur[1] + dy[i]
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            continue
        if graph[nx][ny] == '#':
            continue
        if day1[nx][ny] >= 0:
            continue
        day1[nx][ny] = day1[cur[0]][cur[1]] + 1
        q1.append((nx, ny))


for i in range(r):
    for j in range(c):
        if graph[i][j] == 'J':
            day2[i][j] = 0
            q2.append((i, j))

while q2:
    cur = q2.popleft()
    for i in range(4):
        nx = cur[0] + dx[i]
        ny = cur[1] + dy[i]
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            print(day2[cur[0]][cur[1]] + 1)
            exit()
        if graph[nx][ny] == '#':
            continue
        if day2[nx][ny] >= 0:
            continue
        if day1[nx][ny] != -1 and day1[nx][ny] <= day2[cur[0]][cur[1]] + 1:
            continue
        day2[nx][ny] = day2[cur[0]][cur[1]] + 1
        q2.append((nx, ny))

print("IMPOSSIBLE")
            
