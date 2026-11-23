n = int(input())

arr = [64]

while True:
    if sum(arr) > n:
        arr.sort()
        data = arr.pop(0)
        new_data = data // 2
        if sum(arr) + new_data >= n:
            arr.append(new_data)
        else:
            arr.append(new_data)
            arr.append(new_data)
    elif sum(arr) == n:
        print(len(arr))
        break