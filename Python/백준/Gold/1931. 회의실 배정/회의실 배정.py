
meeting = []

for _ in range(int(input())):
    meeting.append(tuple(map(int, input().split())))

meeting.sort(key=lambda x: (x[1], x[0]))

start_index = 0
end_time = 0
meeting_cnt = 0

while True:
    if start_index >= len(meeting):
        break

    if end_time <= meeting[start_index][0]:
        end_time = meeting[start_index][1]
        meeting_cnt += 1

    start_index += 1

print(meeting_cnt)