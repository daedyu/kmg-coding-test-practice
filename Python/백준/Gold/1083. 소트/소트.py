import sys

input = sys.stdin.readline

def max_idx(main, arr):
    max = -1
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
    if max == -1:
        return 0
    return main.index(max)

n = int(input())

arr = list(map(int, input().split()))

c = int(input())

max = 0
index = 0

for i in range(n -1):
    if c == 0:
        break
    max_index = max_idx(arr, arr[i:i+c+1])
    for j in range(max_index, i - 1, -1):
        if c == 0:
            break
        if j - 1 < 0:
            break
        if arr[j] > arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            c -= 1

print(*arr)