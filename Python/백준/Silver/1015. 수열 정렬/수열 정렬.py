n = int(input())
arr = list(map(int, input().split()))
arr2 = arr.copy()

arr2.sort()

for i in arr:
    index = arr2.index(i)
    print(index, end=' ')
    arr2[index] = -1