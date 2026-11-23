n, m, r = map(int, input().split())

arr = list(map(int, input().split()))
MAX = 16

graph = [[MAX] * n for _ in range(n)]

for _ in range(r):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = c
    graph[b-1][a-1] = c


dp = [[MAX] * n for _ in range(n)]


for i in range(n):
    for j in range(n):
        dp[i][j] = graph[i][j]

for i in range(n):
    dp[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

result = 0

for i in range(n):
    temp = 0
    for j in range(n):
        if dp[i][j] <= m:
            temp += arr[j]
    if temp > result:
        result = temp
print(result)