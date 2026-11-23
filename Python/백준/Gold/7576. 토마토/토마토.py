from collections import deque

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(m)]

result = 0

queue = deque()

for i in range(m):
    for j in range(n):
        if arr[i][j] == 1:
            queue.append((i, j))

time = 0

while queue:
    i, j = queue.popleft()
    for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < m and 0 <= nj < n and arr[ni][nj] == 0:
            arr[ni][nj] = arr[i][j] + 1
            queue.append((ni, nj))

for i in arr:
    for j in i:
        if j == 0:
            print(-1)
            exit()
    result = max(result, max(i))

print(result-1)