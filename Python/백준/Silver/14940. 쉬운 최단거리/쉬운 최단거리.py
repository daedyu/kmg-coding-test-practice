from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
visited = [[False] * m for _ in range(n)]

for _ in range(n):
    arr.append(list(map(int, input().split())))

queue = deque()

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            queue.append((i, j))
            arr[i][j] = 0
            break

while queue:
    i, j = queue.popleft()
    for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 1 and not visited[ni][nj]:
            arr[ni][nj] = arr[i][j] + 1
            visited[ni][nj] = True
            queue.append((ni, nj))

for i in range(n):
    for j in range(m):
        if arr[i][j] != 0 and not visited[i][j]:
            print(-1, end=' ')
        else:
            print(arr[i][j], end=' ')
    print()