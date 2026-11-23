import sys

input = sys.stdin.readline

n, p, q = map(int, input().split())

dp_arr = {0: 1, 1: 2}

def dp(i):
    if dp_arr.get(i) is not None:
        return dp_arr[i]
    if i == 0:
        return 1
    elif i == 1:
        return 2
    dp_arr[i] = dp(i//p) + dp(i//q)
    return dp_arr[i]

print(dp(n))