n = int(input())
m = int(input())

INF = int(1e9)

graph = [[INF] * n for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    if graph[a-1][b-1] > c:
        graph[a-1][b-1] = c

dp = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        dp[i][j] = graph[i][j]

for i in range(n):
    dp[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

for i in dp:
    for j in i:
        if j == INF:
            print(0, end=' ')
        else:
            print(j, end=' ')
    print()