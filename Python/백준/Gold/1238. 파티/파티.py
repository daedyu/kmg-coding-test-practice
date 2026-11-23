import heapq
import sys
input = sys.stdin.readline

def dijkstra(graph, start, end = None):

    INF = int(1e9)
    distance = [INF] * (len(graph) + 1)
    distance[start] = 0

    queue = [(0, start)]

    while queue:
        dist, node = heapq.heappop(queue)
        if dist > distance[node]:
            continue
        for adjacent, weight in graph[node]:
            new_dist = dist + weight
            if new_dist < distance[adjacent]:
                distance[adjacent] = new_dist
                heapq.heappush(queue, (new_dist, adjacent))
    if end is not None:
        return distance[end]
    return distance

n, m, x = map(int, input().split())

graph = {i:[] for i in range(1, n+1)}

for _ in range(m):
    start, end, time = map(int, input().split())
    graph[start].append((end, time))

distance_from_x = dijkstra(graph, x)[1::]

max_value = 0
for i in range(1, n+1):
    temp_value = dijkstra(graph, i, x) + distance_from_x[i-1]
    if temp_value > max_value:
        max_value = temp_value
print(max_value)