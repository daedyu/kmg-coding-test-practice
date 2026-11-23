import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())

arr = []

for _ in range(n):
    arr.append(list(map(int, list(input().rstrip()))))

queue = deque([(0, 0, 1, False)])
visited = [[[False, False] for _ in range(m)] for _ in range(n)]

while queue:
    i, j, step, flag = queue.popleft()
    if i == n-1 and j == m-1:
        print(step)
        exit()
    for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        ni, nj = i + di, j + dj
        if flag:
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj][1]:
                if arr[ni][nj] == 0:
                    queue.append((ni, nj, step+1, flag))
                    visited[ni][nj][1] = True
        else:
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj][0]:
                if arr[ni][nj] == 1:
                    queue.append((ni, nj, step+1, True))
                    visited[ni][nj][1] = True
                else:
                    queue.append((ni, nj, step+1, flag))
                    visited[ni][nj][0] = True

print(-1)