import sys
from collections import defaultdict
input = sys.stdin.readline

graph = defaultdict(set)

n = int(input())

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

result = [0 for _ in range(n)]

visited = set()
stack = [1]
while stack:
    vertex = stack.pop()
    if vertex not in visited:
        for i in graph[vertex]:
            if result[i-1] == 0:
                result[i-1] = vertex
        visited.add(vertex)
        stack += list(graph[vertex])

result.pop(0)

print(*result)