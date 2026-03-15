import sys
from collections import deque


def bfs(root):
    q = deque()
    q.append(root)
    p[root] = -1
    while q:
        cur = q.popleft()
        for next in adj[cur]:
            if p[next] == 0:
                p[next] = cur
                q.append(next)

n = int(input())
p = [0] * (n + 1)
adj = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = list(map(int, sys.stdin.readline().split()))
    adj[u].append(v)
    adj[v].append(u)

bfs(1)
for x in p[2:]:
    print(x)