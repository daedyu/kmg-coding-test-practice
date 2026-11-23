MAX_VALUE = 1000000007

dp = dict()

dp[0] = 0
dp[1] = 1
dp[2] = 1

def fibo(n):
    if dp.get(n) is not None:
        return dp[n]
    if n % 2 == 0:
        temp = fibo(n // 2)
        dp[n] = temp * (2 * fibo(n // 2 + 1) - temp) % MAX_VALUE
        return dp[n]
    else:
        dp[n] = (fibo(n // 2 + 1) ** 2 + fibo(n // 2) ** 2) % MAX_VALUE
        return dp[n]

print(fibo(int(input())))