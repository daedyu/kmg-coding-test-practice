n = input()
arr = list(map(int, input().split()))

def is_prime(n):
    n = abs(n)
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

result = 0
for i in arr:
    if i != 1:
        result += 1 if is_prime(i) else 0

print(result)