n = int(input())
arr = sorted(list(map(int, input().split())))
c = int(input())

i = 0
j = n - 1

result = 0

while i < j:
    if arr[i] + arr[j] == c:
        result += 1
        i += 1
        j -= 1
    elif arr[i] + arr[j] < c:
        i += 1
    else:
        j -= 1

print(result)