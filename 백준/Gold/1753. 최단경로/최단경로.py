import heapq
import sys

data = sys.stdin.read().split()
V, E, start = int(data[0]), int(data[1]), int(data[2])
graph = [[] for _ in range(V+1)]

index = 3
for _ in range(E):
    u, v, w = int(data[index]), int(data[index + 1]), int(data[index + 2])
    graph[u].append((v, w))
    index += 3
  
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

distances = dijkstra(graph, start)
for i in range(1, V+1):
    if distances[i] == float('inf'):
        print("INF")
    else:
        print(distances[i])


