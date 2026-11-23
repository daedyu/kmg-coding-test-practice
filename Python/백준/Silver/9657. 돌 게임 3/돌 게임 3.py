n = int(input())

dp = [0] * (n + 4)

dp[0], dp[1], dp[2], dp[3] = ["SK", "CY", "SK", "SK"]

i = 4

while i < n:
    if dp[i-1] == "CY" or dp[i-3] == "CY" or dp[i-4] == "CY":
        dp[i] = "SK"
    else:
        dp[i] = "CY"
    i += 1

print(dp[n-1])