import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)

v, e = map(int, input().split())
start = int(input())

graph = {i: [] for i in range(1, v+1)}

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

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

for i in range(1, v+1):
    if distance[i] != INF:
        print(distance[i])
    else:
        print("INF")