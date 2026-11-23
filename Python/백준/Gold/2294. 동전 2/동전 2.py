import sys

input = sys.stdin.readline

n, m = map(int, input().split())
dp = [0] * (m + 1)
coins = [0] * n

for i in range(n):
    s = int(input())
    if s > m:
        continue
    dp[s] = 1
    coins[i] = s

coins.sort(reverse=True)

for i in range(1, m + 1):
    min_v = set()
    for coin in coins:
        if dp[i] != 0:
            break
        if i - coin > 0 and dp[i - coin] != 0:
            min_v.add(1 + dp[i - coin])
    if min_v:
        dp[i] = min(min_v)

print(dp[m] if dp[m] else -1)