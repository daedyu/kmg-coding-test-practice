n, r, c = map(int, input().split())

def box_sizing(size, x, y, cnt):
    global r, c

    data = (size // 2) ** 2

    tmp_x = x + size // 2
    tmp_y = y + size // 2

    if size == 1:
        print(cnt)
    elif r < tmp_x and c < tmp_y:
        box_sizing(size // 2, x, y, cnt)
    elif r < tmp_x and tmp_y <= c:
        box_sizing(size // 2, x, tmp_y, cnt + data)
    elif tmp_x <= r and c < tmp_y:
        box_sizing(size // 2, tmp_x, y, cnt + data * 2)
    else:
        box_sizing(size // 2, tmp_x, tmp_y, cnt + data * 3)

box_sizing(2 ** n, 0, 0, 0)