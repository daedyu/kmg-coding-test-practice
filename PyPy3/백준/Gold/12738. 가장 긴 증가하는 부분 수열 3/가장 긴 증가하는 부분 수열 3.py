n = int(input())
arr = list(map(int, input().split()))

dp = [arr[0]]

for i in range(1, n):
    if arr[i] > dp[-1]:
        dp.append(arr[i])
    else:
        left, right = 0, len(dp) - 1
        while left <= right:
            mid = (left + right) // 2
            if dp[mid] < arr[i]:
                left = mid + 1
            else:
                right = mid - 1
        dp[left] = arr[i]

print(len(dp))