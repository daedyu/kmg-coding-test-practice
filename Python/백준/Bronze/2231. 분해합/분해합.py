n = int(input())

result = 0

for i in range(n // 2, n):
    if i + sum(map(int, list(str(i)))) == n:
        result = i
        break

print(result)