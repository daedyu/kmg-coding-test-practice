MOD = 1000000007

n = int(input()) %  MOD

i = 1
value = 1
while True:
    value = value * i % MOD
    if value == n:
        print(i)
        break
    i += 1