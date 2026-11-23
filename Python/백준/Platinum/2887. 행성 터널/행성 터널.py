import sys

def find(a, parents) -> int:
    if parents[a] != a:
        parents[a] = find(parents[a], parents)
    return parents[a]

def union(a, b, parents) -> bool:
    a_p = find(a, parents)
    b_p = find(b, parents)
    if a_p != b_p:
        parents[a_p] = b_p
        return True
    return False

input = sys.stdin.readline

n = int(input())

arr = [None] * n
edges = []

for i in range(n):
    arr[i] = (i, tuple(map(int, input().split())))


def make_edges(k):
    global edges
    arr.sort(key=lambda x: x[1][k])

    for i in range(n - 1):
        s, v = arr[i]
        s2, v2 = arr[i + 1]
        edge = abs(v[k] - v2[k])
        edges.append((s, s2, edge))

make_edges(0)
make_edges(1)
make_edges(2)

edges.sort(key= lambda x: x[2])

total_cost = 0
parents = [i for i in range(n)]
node_cost = 0

for n1, n2, c in edges:
    if union(n1, n2, parents):
        total_cost += c

print(total_cost)