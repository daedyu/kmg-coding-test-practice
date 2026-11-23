import heapq

for _ in range(int(input())):
    n = int(input())

    min_heap = []
    max_heap = []

    visited = set()

    for i in range(n):
        inputs = input().split()
        if inputs[0] == 'I':
            heapq.heappush(min_heap, (int(inputs[1]), i))
            heapq.heappush(max_heap, (-int(inputs[1]), i))
        else:
            if min_heap and max_heap:
                if int(inputs[1]) == 1:
                    data = heapq.heappop(max_heap)
                    while data[1] in visited and max_heap:
                        data = heapq.heappop(max_heap)
                    visited.add(data[1])
                else:
                    data = heapq.heappop(min_heap)
                    while data[1] in visited and min_heap:
                        data = heapq.heappop(min_heap)
                visited.add(data[1])

    if min_heap and max_heap:
        is_empty = False
        max_v = heapq.heappop(max_heap)
        while max_v[1] in visited:
            if not max_heap:
                print("EMPTY")
                is_empty = True
                break
            max_v = heapq.heappop(max_heap)
        min_v = heapq.heappop(min_heap)
        while min_v[1] in visited and not is_empty:
            if not min_heap:
                print("EMPTY")
                is_empty = True
                break
            min_v = heapq.heappop(min_heap)

        if not is_empty:
            print(-max_v[0], min_v[0])
    else:
        print("EMPTY")
