p1 = int(input())

arr = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

def tic_tac_tock():
    if arr[0][0] == arr[1][1] == arr[2][2] != 0:
        return arr[0][0]
    elif arr[0][2] == arr[1][1] == arr[2][0] != 0:
        return arr[1][1]
    elif arr[0][0] == arr[1][0] == arr[2][0] != 0:
        return arr[0][0]
    elif arr[0][1] == arr[1][1] == arr[2][1] != 0:
        return arr[1][1]
    elif arr[0][2] == arr[1][2] == arr[2][2] != 0:
        return arr[0][2]
    elif arr[0][0] == arr[0][1] == arr[0][2] != 0:
        return arr[0][0]
    elif arr[1][0] == arr[1][1] == arr[1][2] != 0:
        return arr[1][1]
    elif arr[2][0] == arr[2][1] == arr[2][2] != 0:
        return arr[2][2]
    return None

p2 = 1 if p1 == 2 else 2

for i in range(9):
    x, y = map(int, input().split())
    arr[x-1][y-1] = p1 if i % 2 == 0 else p2
    if i >= 2:
        v = tic_tac_tock()
        if v is not None:
            print(tic_tac_tock())
            exit()

print(0)