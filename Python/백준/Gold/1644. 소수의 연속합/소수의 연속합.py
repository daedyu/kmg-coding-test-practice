import array

def is_prime(p):
    if p == 2 or p == 3:
        return True
    if p % 2 == 0 or p % 3 == 0:
        return False
    d = p - 1
    s = 0

    while (d & 1) == 0:
        d >>= 1
        s += 1

    for a in [2, 7, 61]:
        if a >= p:
            continue
        x = pow(a, d, p)
        if x == 1 or x == p - 1:
            continue
        is_not_prime = True
        for _ in range(s-1):
            x = (x * x) % p
            if x == p - 1:
                is_not_prime = False
                break
        if is_not_prime:
            return False
    return True

n = int(input())

prime_sums = array.array('l', [0, 2])

for i in range(3, n + 1):
    if is_prime(i):
        prime_sums.append(i + prime_sums[-1])

i, j = 0, 0

result = 0

lens = len(prime_sums)

while i < lens and j < lens:
    if prime_sums[j] - prime_sums[i] == n:
        result += 1
        j += 1
    elif prime_sums[j] - prime_sums[i] < n:
        j += 1
    else:
        i += 1

print(result)