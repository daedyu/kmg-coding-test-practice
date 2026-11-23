n = int(input())

tree = {i: [] for i in range(n)}

root = None

data = enumerate(map(int, input().split()))
delete_node = int(input())

for i, parent in data:
    if parent == -1:
        root = i
        continue
    if parent != delete_node and i != delete_node:
        tree[parent].append(i)

tree[delete_node] = None
stack = list()
stack.append(root)
leaf = 0

while stack:
    node = tree[stack.pop()]
    if node is None:
        continue
    if len(node) == 0:
        leaf += 1
        continue

    stack += node[::-1]

print(leaf)