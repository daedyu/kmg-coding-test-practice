N, K = map(int, input().split())

items = list()

for _ in range(N):
    w, v = map(int, input().split())
    items.append((w, v))

dp = [[0] * (K + 1) for _ in range(N + 1)]

for n in range(N):
    for k in range(K+1):
        prev_k = k - items[n][0]
        case1 = 0
        if 0 <= prev_k:
            case1 = dp[n - 1][prev_k] + items[n][1]
        case2 = dp[n - 1][k]
        dp[n][k] = max(case1, case2)

print(dp[N - 1][K])