
n = int(input())

for _ in range(n):
    k = int(input()) + 1
    n = int(input())
    dp = [[0] * n for _ in range(k)]
    for i in range(1, n + 1):
        dp[0][i - 1] = i

    for i in range(1, k):
        for j in range(n):
            dp[i][j] = sum(dp[i - 1][:j + 1])
    print(dp[k - 1][n - 1])