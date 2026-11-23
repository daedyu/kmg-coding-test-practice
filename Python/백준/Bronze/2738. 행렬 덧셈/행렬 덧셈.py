n, m = map(int, input().split())

arr = []
arr2 = []
for i in range(n):
    arr.append(list(map(int, input().split())))
for i in range(n):
    arr2.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        print(arr[i][j] + arr2[i][j], end=' ')
    print()