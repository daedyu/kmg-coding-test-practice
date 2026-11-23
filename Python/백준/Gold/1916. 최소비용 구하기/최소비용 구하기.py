import heapq

n = int(input())
m = int(input())

graph = {i:[] for i in range(1, n+1)}

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

INF = int(1e9)

distance = [INF] * (n + 1)

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

print(distance[end])