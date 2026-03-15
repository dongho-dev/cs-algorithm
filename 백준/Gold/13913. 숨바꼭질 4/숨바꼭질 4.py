import sys
from collections import deque

move = [2, -1, 1]

n, k = map(int, sys.stdin.readline().strip().split())
dist = [-1] * 100001
parent = [-1] * 100001
q = deque()

dist[n] = 0
q.append(n)

a = k
rev = [] 
while q:
    cur = q.popleft()
    if cur == k:
        print(dist[cur])
        while a != -1:
            rev.append(a)
            a = parent[a]
        rev.reverse()
        for x in rev:
            print(x, end=" ")
        exit()
    for i in range(3):
        if i == 0:
            nx = cur * move[i]
        else:
            nx = cur + move[i]
        if nx < 0 or nx > 100000:
            continue
        if dist[nx] >= 0:
            continue
        dist[nx] = dist[cur] + 1
        parent[nx] = cur
        q.append(nx)
