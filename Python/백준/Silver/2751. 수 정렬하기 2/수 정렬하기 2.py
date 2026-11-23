import sys
input = sys.stdin.readline
n = int(input())
arr: list = [0] * n
for i in range(n):
    arr[i] = (int(input()))
arr.sort()
print(*arr, sep="\n")