n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, list(input()))))

def makeZero(i, j):
    if i < 0 or i >= n or j < 0 or j >= n:
        return 0
    global arr
    if arr[i][j] == 0:
        return 0
    arr[i][j] = 0
    result = 1
    result += makeZero(i-1, j)
    result += makeZero(i+1, j)
    result += makeZero(i, j-1)
    result += makeZero(i, j+1)
    return result

def findOne():
    global arr
    for i in range(n):
        if sum(arr[i]) != 0:
            for j in range(n):
                if arr[i][j] == 1:
                    return i, j
    return -10, -10

result = 0

dong = []

while True:
    i, j = findOne()
    if i == -10:
        break
    result += 1
    dong.append(makeZero(i, j))

print(result)
print(*sorted(dong), sep='\n')