count_arr = dict()
name_arr = dict()

n, m = map(int, input().split())

for i in range(1, n + 1):
    name = input()
    count_arr[str(i)] = name
    name_arr[name] = str(i)

for _ in range(m):
    name_or_arr = input()
    if name_or_arr.isdigit():
        print(count_arr[name_or_arr])
    else:
        print(name_arr[name_or_arr])
