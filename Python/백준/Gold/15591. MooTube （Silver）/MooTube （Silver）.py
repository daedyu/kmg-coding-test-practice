def dfs(graph: dict, start: int, k: int):
    visited = set()
    stack = [(start, 0)]
    result = -1
    while stack:
        node, weight = stack.pop()
        if node not in visited:
            visited.add(node)
            if node == start or weight >= k:
                result += 1
                for i, s in graph[node]:
                    stack.append((i, s))
    return result

n, m = map(int, input().split())

graph = {i: [] for i in range(1, n+1)}


for _ in range(n-1):
    p, q, r = map(int, input().split())
    graph[p].append((q, r))
    graph[q].append((p, r))

for _ in range(m):
    k, v = map(int, input().split())

    print(dfs(graph, v, k))