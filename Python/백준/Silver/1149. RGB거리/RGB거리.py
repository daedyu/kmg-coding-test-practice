n = int(input())

dp = [(0, 0, 0) for _ in range(n)]

first, second, third = map(int, input().split())

dp[0] = (first, second, third)

for i in range(1, n):
    first, second, third = map(int, input().split())
    f_dp = first + min(dp[i-1][1], dp[i-1][2])
    s_dp = second + min(dp[i-1][0], dp[i-1][2])
    t_dp = third + min(dp[i-1][0], dp[i-1][1])
    dp[i] = (f_dp, s_dp, t_dp)

print(min(dp[n-1]))