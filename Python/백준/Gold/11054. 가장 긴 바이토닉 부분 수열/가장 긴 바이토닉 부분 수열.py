n = int(input())

arr = list(map(int, input().split()))

dp = [1] * n

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[j] + 1, dp[i])

dp2 = [1] * n

for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if arr[i] > arr[j]:
            dp2[i] = max(dp2[j] + 1, dp2[i])

result = [x + y - 1 for x, y in zip(dp, dp2)]

print(max(result))