import heapq
import sys
input = sys.stdin.readline

def dijkstra(start, end, graph):
    distance = [INF] * (v + 1)

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
    return distance[end]

INF = int(1e9)

v, e = map(int, input().split())

graph = {i: [] for i in range(1, v+1)}

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

must_visit1, must_visit2 = map(int, input().split())

a = dijkstra(1, must_visit1, graph)
b = dijkstra(1, must_visit2, graph)
min_const_from_must_visit = dijkstra(must_visit1, must_visit2, graph)
a_to_end = dijkstra(must_visit1, v, graph)
b_to_end = dijkstra(must_visit2, v, graph)

result = min(a + min_const_from_must_visit + b_to_end,
             b + min_const_from_must_visit + a_to_end)
if result >= INF:
    result = -1
print(result)