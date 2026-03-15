import sys
import heapq

data = sys.stdin.read().split()
N, E = int(data[0]), int(data[1])
graph = [[] for _ in range(N + 1)]
index = 2
for i in range(E):
    u, v, w = int(data[index]), int(data[index + 1]), int(data[index + 2])
    graph[u].append((v, w))
    graph[v].append((u, w))
    index += 3
v1, v2 = int(data[index]), int(data[index + 1])

def dijkstra(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        distance, cur = heapq.heappop(q)
        if dist[cur] < distance:
            continue
        for neighbor, weight in graph[cur]:
            cost = distance + weight
            if cost < dist[neighbor]:
                dist[neighbor] = cost
                heapq.heappush(q, (cost, neighbor))
    return dist

distances = dijkstra(graph, 1)
distances2 = dijkstra(graph, v1)
distances3 = dijkstra(graph, v2)

r1 = distances[v1] + distances2[v2] + distances3[N]
r2 = distances[v2] + distances3[v1] + distances2[N]

result = min(r1, r2)
if result >= float('inf'):
    print(-1)
else:
    print(result)