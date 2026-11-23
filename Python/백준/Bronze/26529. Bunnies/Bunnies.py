dp = [0] * 46

dp[0] = 1
dp[1] = 1

value = []

for _ in range(int(input())):
    value.append(int(input()))

for i in range(2, max(value) + 1):
    dp[i] = dp[i-1] + dp[i-2]

for i in value:
    print(dp[i])
