from collections import deque

start, end = map(int, input().split())

queue = deque([(start, 1)])

while queue:
    number, depth = queue.popleft()
    if number == end:
        print(depth)
        exit()

    for i in [number * 10 + 1, number * 2]:
        if i <= end:
            queue.append((i, depth+1))

print(-1)