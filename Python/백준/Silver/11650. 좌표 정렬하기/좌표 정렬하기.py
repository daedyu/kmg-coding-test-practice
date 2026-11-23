arr = []

for _ in range(int(input())):
    a, b = map(int, input().split())
    arr.append((a, b))

arr.sort(key=lambda x: (x[0], x[1]))

for i in range(len(arr)):
    print(arr[i][0], arr[i][1])