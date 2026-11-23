MAX_VALUE = 1000000000

DP = dict()

DP[0] = 0
DP[1] = 1
DP[2] = 1

def fibonacci(n):
    if DP.get(n) is not None:
        return DP[n]
    if n % 2 == 0:
        k = n // 2
        DP[n] = fibonacci(n // 2) * (2 * fibonacci(k + 1) - fibonacci(k)) % MAX_VALUE
        return DP[n]
    else:
        k = (n - 1) // 2
        DP[n] = (fibonacci(k + 1) ** 2 + fibonacci(k) ** 2) % MAX_VALUE
        return DP[n]

n, m = map(int, input().split())

print((fibonacci(m + 2) % MAX_VALUE - fibonacci(n + 1) % MAX_VALUE) % MAX_VALUE)