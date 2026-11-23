n = int(input())
node = int(input())

arr = {i: [] for i in range(1, n+1)}

for i in range(node):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)


visited = set()
queue = [1]

while queue:
    current = queue.pop(0)
    visited.add(current)
    for i in arr[current]:
        if i not in visited:
            queue.append(i)

print(len(visited)-1)