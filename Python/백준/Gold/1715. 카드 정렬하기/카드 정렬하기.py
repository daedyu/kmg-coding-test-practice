import heapq

n = int(input())
arr = []

for _ in range(n):
    heapq.heappush(arr, int(input()))

result = 0

while len(arr) > 1:
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    merged = a + b
    result += merged
    heapq.heappush(arr, merged)

print(result)