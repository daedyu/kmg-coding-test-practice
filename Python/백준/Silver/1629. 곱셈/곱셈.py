def pow(a, n, c):
    if n == 1:
        return a % c
    if n % 2 == 0:
        result = pow(a, n // 2, c)
        return (result * result) % c
    else:
        result = pow(a, (n - 1) // 2, c)
        return (a * result * result) % c

a, b, c = map(int, input().split())

print(pow(a, b, c))