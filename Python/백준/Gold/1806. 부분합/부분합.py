import array
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = array.array('i', list(map(int, input().split())))

dp = array.array('i', [0] * (n + 1))

dp[1] = arr[0]

for i in range(1, n):
    dp[i + 1] = dp[i] + arr[i]

start, end = 0, 0

min = int(1e9)

while start <= n and end <= n:
    if dp[end] - dp[start] >= m and end - start < min:
        min = end - start
    if start == end and arr[start - 1] > m:
        print(1)
        exit()
    if dp[end] - dp[start] < m:
        end += 1
    else:
        start += 1

if min == int(1e9):
    print(0)
else: 
    print(min)