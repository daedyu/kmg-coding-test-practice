n = int(input())

arr = set()

for _ in range(n):
    arr.add(input())
a = sorted(list(arr), key= lambda x: (len(x), x))

print(*a, sep='\n')
