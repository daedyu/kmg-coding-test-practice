import heapq

n = int(input())

class_room = [0]

studies = [tuple(map(int, input().split())) for _ in range(n)]

studies.sort(key=lambda x: x[1])

for study in studies:
    min_v = heapq.heappop(class_room)
    if min_v <= study[1]:
        heapq.heappush(class_room, study[2])
    else:
        heapq.heappush(class_room, min_v)
        heapq.heappush(class_room, study[2])

print(len(class_room))