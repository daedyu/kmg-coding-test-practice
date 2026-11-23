import math

n = int(input())

arr = list()

for _ in range(n):
    arr.append(tuple(map(int, input().split())))

A, B = 0, 0

for i in range(n):
    if i == n-1:
        A += arr[i][0] * arr[0][1]
        B += arr[0][0] * arr[i][1]
    else:
        A += arr[i][0] * arr[i+1][1]
        B += arr[i+1][0] * arr[i][1]

print(abs(A - B) / 2)