import sys
input = sys.stdin.readline

n = int(input())
max_v = dict()
arr = []

for _ in range(n):
    k = int(input())
    arr.append(k)
    if k in max_v.keys():
        max_v[k] = max_v.get(k) + 1
    else:
        max_v[k] = 1

arr.sort()

print(round(sum(arr) / n))
print(arr[n//2])
keys = [k for k in max_v if max_v[k] == max(max_v.values())]

keys.sort()

print(keys[1] if len(keys) > 1 else keys[0])
print(arr[-1] - arr[0])