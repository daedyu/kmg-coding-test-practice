def circle_size(x1, y1, r1, x2, y2, r2):
    d2 = (x1 - x2) ** 2 + (y1 - y2) ** 2

    if d2 == 0 and r1 == r2:
        return -1

    if d2 <= (r1 - r2) ** 2:
        length = (r1 - r2) ** 2
        if d2 == length:
            return 1
        elif d2 < length:
            return 0
        else:
            return 2
    else:
        length = (r1 + r2) ** 2
        if d2 > length:
            return 0
        elif d2 == length:
            return 1
        else:
            return 2

for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    print(circle_size(x1, y1, r1, x2, y2, r2))