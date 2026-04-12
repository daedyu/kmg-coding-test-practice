import sys
from collections import deque

input = sys.stdin.readline

queue = deque()

for _ in range(int(input())):
    cmd = list(input().split())
    if cmd[0] == 'push':
        queue.append(cmd[1])
    if cmd[0] == 'pop':
        if not queue:
            print(-1)
        else: print(queue.popleft())
    if cmd[0] == 'size':
        print(len(queue))
    if cmd[0] == 'empty':
        print(0 if queue else 1)
    if cmd[0] == 'front':
        print(-1 if not queue else queue[0])
    if cmd[0] == 'back':
        print(-1 if not queue else queue[-1])