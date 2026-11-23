n, m = map(int, input().split())
arr = list(map(int, input().split()))
dp = [0] * n

dp[0] = arr[0]

for i in range(1, n):
    dp[i] = dp[i-1] + arr[i]

for _ in range(m):
    a, b = map(int, input().split())
    a -= 2
    b -= 1
    print((dp[b] if b >= 0 else 0) - (dp[a] if a >= 0 else 0))