import sys

input = sys.stdin.readline

n, m, q = map(int, input().split())
arr = list(map(int, input().split()))

size = {}
clean_counts = {}

parent = [i for i in range(n + 1)]

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a_p = find(a)
    b_p = find(b)
    if a_p > b_p:
        parent[a_p] = b_p
        size[parent[a_p]] = size.get(a_p, 1) + size.get(parent[b_p], 1)
        clean_counts[parent[a_p]] = clean_counts.get(a_p, arr[a_p - 1]) + clean_counts.get(parent[b_p], arr[parent[b_p] - 1])
    elif a_p < b_p:
        parent[b_p] = a_p
        size[parent[b_p]] = size.get(b_p, 1) + size.get(parent[a_p], 1)
        clean_counts[parent[b_p]] = clean_counts.get(b_p, arr[b_p - 1]) + clean_counts.get(parent[a_p], arr[parent[a_p] - 1])

for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

for _ in range(q):
    found = find(int(input()))
    print(1 if size.get(found, 1) // 2 < clean_counts.get(found, arr[found - 1]) else 0)
