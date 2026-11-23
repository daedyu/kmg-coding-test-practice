from collections import defaultdict

n, m ,v = map(int, input().split())

arr = defaultdict(list)

def dfs(graph: defaultdict, start):
    visited = set()
    stack = [start]
    while stack:
        vertex = stack.pop(0)
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            n = graph[vertex]
            n.sort()
            stack = n + stack

def bfs(graph: defaultdict, start):
    visited = set()
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            n = graph[vertex]
            n.sort()
            queue += n

for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

dfs(arr, v)
print()
bfs(arr, v)