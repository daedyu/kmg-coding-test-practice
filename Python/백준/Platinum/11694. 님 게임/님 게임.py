n = int(input())
arr = list(map(int, input().split()))

nim_sum = 0
all_ones = True
for x in arr:
    if all_ones and x > 1: all_ones = False
    nim_sum ^= x

if all_ones:
    if n % 2 == 0:
        print("koosaga")
    else:
        print("cubelover")
else:
    if nim_sum != 0:
        print("koosaga")
    else:
        print("cubelover")