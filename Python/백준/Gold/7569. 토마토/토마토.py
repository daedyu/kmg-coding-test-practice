from collections import deque

n, m, h = map(int, input().split())

arr = [ [list(map(int, input().split())) for __ in range(m)] for _ in range(h) ]

queue = deque()

for i in range(h):
    for j in range(m):
        for k in range(n):
            if arr[i][j][k] == 1:
                queue.append((i, j, k))

result = 0

while queue:
    i, j, k = queue.popleft()
    for di, dj, dk in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
        ni, nj, nk = i + di, j + dj, k + dk
        if 0 <= ni < h and 0 <= nj < m and 0 <= nk < n and arr[ni][nj][nk] == 0:
            arr[ni][nj][nk] = arr[i][j][k] + 1
            queue.append((ni, nj, nk))

for i in arr:
    for j in i:
        if 0 in j:
            print(-1)
            exit()
        result = max(result, max(j))

print(result-1)