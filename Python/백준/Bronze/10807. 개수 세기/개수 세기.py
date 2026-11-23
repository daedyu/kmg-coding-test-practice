n = int(input())
arr = list(map(int, input().split()))
result = 0
k = int(input())
for i in range(n):
    if arr[i] == k: result += 1
print(result)