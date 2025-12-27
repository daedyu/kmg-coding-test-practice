arr = []
for _ in range(int(input())):
    arr.append(int(input()))

arr.sort()

print(*arr, sep="\n")