from math import sqrt

n, m = map(int, input().split())


for i in range(n, m + 1):
    isPrime = True
    for j in range(2, int(sqrt(i)) + 1):
        if i % j == 0:
            isPrime = False
            break
    if isPrime and i != 1:
        print(i)