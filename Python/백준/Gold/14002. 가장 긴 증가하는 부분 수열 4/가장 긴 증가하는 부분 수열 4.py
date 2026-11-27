n = int(input())

arr = list(map(int, input().split()))

dp = [1] * n

dicts = {}

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[j] + 1, dp[i])

max_num = max(dp)
index = dp.index(max_num)

print(max_num)
max_num-=1

result = [arr[index]]

for i in range(index-1, -1, -1):
    if arr[index] > arr[i] and dp[i] == max_num:
        result.append(arr[i])
        max_num -= 1

print(*result[::-1], sep=' ')