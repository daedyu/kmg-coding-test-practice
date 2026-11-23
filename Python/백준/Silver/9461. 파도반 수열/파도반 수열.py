dp = [0] * 101
dp[0] = 1
dp[1] = 1
dp[2] = 1
dp[3] = 2
dp[4] = 2

for _ in range(int(input())):
    n = int(input())
    if dp[n] == 0:
        for i in range(5, n):
            dp[i] = dp[i-1] + dp[i-5]
    print(dp[n-1])
