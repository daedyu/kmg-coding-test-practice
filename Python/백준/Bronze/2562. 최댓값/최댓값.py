min_v = 0
min_i = 0

for i in range(9):
    n = int(input())
    if n > min_v:
        min_v = n
        min_i = i
print(min_v)
print(min_i + 1)