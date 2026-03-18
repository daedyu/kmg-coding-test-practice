n = int(input())

arr = list(map(int, input().split()))

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

lit = [arr[0]]

for i in range(len(arr)):
    if arr[i] > lit[-1]:
        lit.append(arr[i])
    else:
        index = binary_search(lit, arr[i])
        lit[index] = arr[i]

print(len(lit))