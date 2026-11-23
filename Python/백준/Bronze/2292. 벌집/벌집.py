dp = [[1, 0]]

n = int(input())

i = 0

while True:
    if dp[i][0] >= n:
        break
    i += 1
    dp.append([dp[i-1][0] + ((dp[i-1][1] + 1) * 6), dp[i-1][1] + 1])

print(dp[-1][1] + 1)