n = int(input())

s = list([0])

for _ in range(n):
    s.append(int(input()))


if n <= 2:
    print(sum(s))
    exit()

dp = [0] * (n + 1)

dp[0] = 0
dp[1] = s[1]
dp[2] = s[2] + s[1]

for i in range(3, n+1):
    dp[i] = max(s[i] + s[i-1] + dp[i-3], s[i] + dp[i-2])

print(dp[n])