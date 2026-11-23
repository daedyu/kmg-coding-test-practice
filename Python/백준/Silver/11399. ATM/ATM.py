n = int(input())
arr = list(map(int, input().split()))

arr.sort()

dp = [0] * n

for i in range(n):
    if i == 0:
        dp[i] = arr[i]
        continue
    dp[i] = dp[i-1] + arr[i]

print(sum(dp))