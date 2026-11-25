x, y, w, h = list(map(int, input().split(' ')))

arr = []

arr.append(x)
arr.append(y)
arr.append(w-x)
arr.append(h-y)

print(min(arr))