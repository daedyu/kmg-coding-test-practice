n, k = map(int, input().split())
mod = 1_000_000_007

k = min(k, n - k)
numerator: int = 1
denominator: int = 1

for i in range(1, k + 1):
    numerator = numerator * (n - i + 1) % mod
    denominator = denominator * i % mod

print(numerator * pow(denominator, mod - 2, mod) % mod)