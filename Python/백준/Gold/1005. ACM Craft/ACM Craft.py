import sys
input = sys.stdin.readline

def get_by_dp(w):
    if dp[w] != -1:
        return dp[w]
    if work_life.get(w) is None:
        dp[w] = time[w - 1]
    else:
        max_time = 0
        for prev in work_life[w]:
            max_time = max(max_time, get_by_dp(prev))
        dp[w] = max_time + time[w - 1]
    return dp[w]

for _ in range(int(input())):
    n, k = map(int, input().split())
    time = list(map(int, input().split()))

    work_life = dict()

    for i in range(k):
        prev, next = map(int, input().split())
        if work_life.get(next) is None:
            work_life[next] = [prev]
        else:
            work_life[next].append(prev)
    w = int(input())

    dp = [-1] * (n + 1)

    dp[0] = 0
    print(get_by_dp(w))