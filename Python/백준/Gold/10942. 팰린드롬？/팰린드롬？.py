import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

dp = [[0] * n for _ in range(n)]

for i in range(n):
    dp[i][i] = 1

for i in range(n - 1):
    if arr[i] == arr[i + 1]:
        dp[i][i+1] = 1

for i in range(3, n + 1):
    for start in range(n - i + 1):
        last = start + i - 1
        if arr[start] == arr[last] and dp[start + 1][last - 1] == 1:
            dp[start][last] = 1

for i in range(int(input())):
    a, b = map(int, input().split())
    print(dp[a-1][b-1])