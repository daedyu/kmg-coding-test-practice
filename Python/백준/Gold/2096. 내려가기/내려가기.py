n = int(input())

dp_max = [0, 0, 0]
dp_min = [0, 0, 0]

for _ in range(n):
    arr = list(map(int, input().split()))
    tmp_max = dp_max.copy()
    tmp_min = dp_min.copy()
    dp_max[0] = max(tmp_max[0], tmp_max[1]) + arr[0]
    dp_max[1] = max(tmp_max) + arr[1]
    dp_max[2] = max(tmp_max[1], tmp_max[2]) + arr[2]

    dp_min[0] = min(tmp_min[0], tmp_min[1]) + arr[0]
    dp_min[1] = min(tmp_min) + arr[1]
    dp_min[2] = min(tmp_min[1], tmp_min[2]) + arr[2]

print(max(dp_max), min(dp_min))