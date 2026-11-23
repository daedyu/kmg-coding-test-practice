n = int(input())
arr = list(map(int, input().split()))

prefix = [0] * (n + 1)
for i in range(n):
    prefix[i+1] = prefix[i] + arr[i]

stack = []
max_value = 0
start, end = 0, 0

for i in range(n):
    while stack and arr[stack[-1]] > arr[i]:
        idx = stack.pop()
        height = arr[idx]

        if stack:
            left = stack[-1] + 1
        else:
            left = 0

        right = i - 1

        total = prefix[right+1] - prefix[left]
        max_value = max(max_value, total * height)
        if max_value == total * height:
            start = left
            end = right

    stack.append(i)

while stack:
    idx = stack.pop()
    height = arr[idx]

    if stack:
        left = stack[-1] + 1
    else:
        left = 0

    right = n - 1

    total = prefix[right+1] - prefix[left]
    max_value = max(max_value, total * height)
    if max_value == total * height:
        start = left
        end = right

print(max_value)
print(start + 1, end + 1)