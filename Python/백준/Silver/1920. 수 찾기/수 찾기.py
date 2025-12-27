dict_nums = dict()

input()

arr = list(map(int, input().split()))

for i in arr:
    dict_nums[i] = i

input()

data = list(map(int, input().split()))

for i in data:
    print(1 if dict_nums.get(i) else 0)