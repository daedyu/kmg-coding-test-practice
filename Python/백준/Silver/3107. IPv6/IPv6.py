arr = input().split(':')

for i in range(8):
    if arr[i] == '':
        if len(arr) < 8:
            arr.pop(i)
            for _ in range(8 - len(arr)):
                arr.insert(i, '0000')
            continue
        elif len(arr) > 8:
            arr.pop(i)
        else:
            arr[i] = '0000'
    if len(arr[i]) < 4:
        arr[i] = '0' * (4 - len(arr[i])) + arr[i]

if len(arr) < 8:
    for _ in range(8 - len(arr)):
        arr.insert(0, '0000')

print(':'.join(arr))