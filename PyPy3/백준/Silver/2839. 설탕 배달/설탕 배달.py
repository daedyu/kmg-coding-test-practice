n = int(input())

dp = [0] * (n+3)

dp[3] = 1
dp[5] = 1

for i in range(3, n+1):
    if dp[i-5] > 0:
        dp[i] = dp[i-5] + 1
    elif dp[i-3] > 0:
        dp[i] = dp[i-3] + 1


print(dp[n] if dp[n] > 0 else -1)