def find(x, arr):
    if arr[x] == x:
        return x
    arr[x] = find(arr[x], arr)
    return arr[x]

def union(a, b, arr):
    a_p = find(a, arr)
    b_p = find(b, arr)
    if a_p > b_p:
        arr[a_p] = b_p
    elif a_p < b_p:
        arr[b_p] = a_p


n, m = map(int, input().split())

nodes = [i for i in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    union(a, b, nodes)

now_time = 0

result = 0

for i in map(int, input().split()):
    finded = find(i, nodes)
    if now_time == 0:
        now_time = finded
    elif now_time != finded:
        result += 1
        now_time = finded

print(result)