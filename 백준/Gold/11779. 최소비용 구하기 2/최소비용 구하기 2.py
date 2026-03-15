import heapq
import sys

data = sys.stdin.read().split()
n, m = int(data[0]), int(data[1])
graph = [[] for _ in range(n + 1)]
index = 2
for _ in range(m):
    u, v, w = int(data[index]), int(data[index + 1]), int(data[index + 2])
    graph[u].append((v, w))
    index += 3
start, arrived = int(data[-2]), int(data[-1])

def dijkstra(graph, start, arrived):
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    parent = [-1] * n
    while q:
        distance, cur = heapq.heappop(q)
        if dist[cur] < distance:
            continue
        for neighbor, weight in graph[cur]:
            cost = distance + weight
            if cost < dist[neighbor]:
                dist[neighbor] = cost
                heapq.heappush(q, (cost, neighbor))
                parent[neighbor] = cur

    path = []
    current = arrived
    while current != -1:
        path.append(current)
        current = parent[current]
    path.reverse()
    return dist[arrived], path

min_cost, path = dijkstra(graph, start, arrived)
print(min_cost)
print(len(path))
print(' '.join(map(str, path)))

