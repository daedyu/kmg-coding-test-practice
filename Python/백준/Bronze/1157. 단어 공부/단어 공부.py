n = list(input())

arr = dict()

for data in n:
    char = data.upper()
    if arr.get(char) is None:
        arr[char] = 1
    else:
        arr[char] += 1

max_value = sorted(list(arr.items()), key=lambda x: x[1], reverse=True)

if len(max_value) > 1 and max_value[0][1] == max_value[1][1]:
    print("?")
else:
    print(max_value[0][0])