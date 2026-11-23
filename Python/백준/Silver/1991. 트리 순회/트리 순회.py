n = int(input())
graph = dict()

for _ in range(n):
    a, b, c = input().split()
    graph[a] = {'l': b, 'r': c}

def preorder(graph, start):
    print(start, end='')
    if graph[start]['l'] != '.':
        preorder(graph, graph[start]['l'])
    if graph[start]['r'] != '.':
        preorder(graph, graph[start]['r'])

def midorder(graph, start):
    if graph[start]['l'] != '.':
        midorder(graph, graph[start]['l'])
    print(start, end='')
    if graph[start]['r'] != '.':
        midorder(graph, graph[start]['r'])

def postorder(graph, start):
    if graph[start]['l'] != '.':
        postorder(graph, graph[start]['l'])
    if graph[start]['r'] != '.':
        postorder(graph, graph[start]['r'])
    print(start, end='')

preorder(graph, 'A')
print()
midorder(graph, 'A')
print()
postorder(graph, 'A')