n = int(input())

arr = [None] * n

for i in range(n):
    arr[i] = tuple(map(int, input().split()))
arr.sort(key= lambda x: (x[1], x[0]))

for i in arr:
    print(*i, sep=' ')