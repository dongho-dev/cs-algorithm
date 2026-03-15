import sys
import heapq

data = sys.stdin.read().split()
N, M = int(data[0]), int(data[1])
graph = [[] for _ in range(N + 1)]
index = 2
for i in range(M):
    u, v, w = int(data[index]), int(data[index + 1]), int(data[index + 2])
    graph[u].append((v, w))
    index += 3
start, end = int(data[index]), int(data[index + 1])

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
print(distances[end])