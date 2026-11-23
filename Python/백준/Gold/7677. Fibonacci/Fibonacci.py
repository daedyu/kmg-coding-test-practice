MAX_VALUE = 10000

DP = dict()

DP[0] = 0
DP[1] = 1
DP[2] = 1

def fibonacci(n):
    global result
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


while True:
    n = int(input())
    if n == -1:
        break
    print(fibonacci(n))