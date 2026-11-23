n = int(input())
data = list(map(int, input().split()))
temp = data[0]
for i in range(1, n):
    temp ^= data[i]

if temp == 0:
    print("cubelover")
else:
    print("koosaga")