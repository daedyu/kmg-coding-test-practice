import sys 

sys.setrecursionlimit(10**6)

def find(a, parents) -> int:
    if parents[a] != a:
        parents[a] = find(parents[a], parents)
    return parents[a]

def union(a, b, parents) -> bool:
    a_p = find(a, parents)
    b_p = find(b, parents)
    if a_p != b_p:
        if a_p > b_p:
            parents[a_p] = parents[b_p]
        else:
            parents[b_p] = parents[a_p]

        return True
    return False

n, m = map(int, input().split())

edges = [None] * m

for i in range(m):
    a, b, c = map(int, input().split())
    edges[i] = (a, b, c)

edges.sort(key=lambda x: x[2])

parents = [i for i in range(n + 1)]

result = 0
edges_count = 0

for n1, n2, c in edges:
    if union(n2, n1, parents):
        result += c
        edges_count += 1
    if edges_count == n-1:
        break

print(result)