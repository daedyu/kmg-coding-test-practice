from collections import deque

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

owner = [[0] * n for _ in range(n)]
dist = [[-1] * n for _ in range(n)]

def make_island(arr, x, y, id):
    queue = deque([(x, y)])
    owner[x][y] = id

    while queue:
        x, y = queue.popleft()
        for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 1 and owner[nx][ny] == 0:
                owner[nx][ny] = id
                queue.append((nx, ny))

idx = 1
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and owner[i][j] == 0:
            make_island(arr, i, j, idx)
            idx += 1

queue = deque()

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            for nx, ny in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0:
                    if dist[i][j] == -1:
                        dist[i][j] = 0
                        queue.append((i, j))
                    break

result = float('inf')

while queue:
    x, y = queue.popleft()
    for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
        if 0 <= nx < n and 0 <= ny < n:
            if owner[nx][ny] == 0 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                owner[nx][ny] = owner[x][y]
                queue.append((nx, ny))
            elif owner[nx][ny] != 0 and owner[nx][ny] != owner[x][y]:
                result = min(result, dist[x][y] + dist[nx][ny])
                
print(result)