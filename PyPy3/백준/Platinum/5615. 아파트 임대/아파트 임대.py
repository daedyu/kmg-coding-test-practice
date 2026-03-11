import sys
input = sys.stdin.readline

def is_prime(p):
    if p == 1:
        return False
    if p == 2 or p == 3:
        return True
    if p % 2 == 0 or p % 3 == 0:
        return False

    d = p - 1
    s = 0
    while (d & 1) == 0:
        d >>= 1
        s += 1

    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:

        if a % p == 0:
            continue

        data = pow(a, d, p)

        if data == 1 or data == p - 1:
            continue

        is_prime_able = False

        for _ in range(s-1):
            data = (data * data) % p
            if data == 1:
                return False
            if data == p - 1:
                is_prime_able = True
                break

        if is_prime_able:
            continue

        return False

    return True

ans = 0

for _ in range(int(input())):
    if is_prime(int(input()) * 2 + 1): ans += 1

print(ans)