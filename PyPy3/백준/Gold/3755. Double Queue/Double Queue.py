import sys
import heapq

input = sys.stdin.readline

min_queue = []
max_queue = []
visited = set()

id = 0

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0: break
    if arr[0] == 1:
        heapq.heappush(min_queue, (arr[2], arr[1], id))
        heapq.heappush(max_queue, (-arr[2], -arr[1], id))
        id += 1
    elif arr[0] == 2:
        if not max_queue:
            print(0)
            continue
        x = heapq.heappop(max_queue)
        while x[2] in visited and max_queue:
            x = heapq.heappop(max_queue)
        if x[2] in visited:
            print(0)
            continue
        visited.add(x[2])
        print(-x[1])
    elif arr[0] == 3:
        if not min_queue:
            print(0)
            continue
        x = heapq.heappop(min_queue)
        while x[2] in visited and min_queue:
            x = heapq.heappop(min_queue)
        if x[2] in visited:
            print(0)
            continue
        visited.add(x[2])
        print(x[1])