n, price = map(int, input().split())

coins = list()

for _ in range(n):
    coins.append(int(input()))

coins.sort(reverse=True)
result = 0
for coin in coins:
    if coin <= price:
        result += price // coin
        price %= coin
print(result)