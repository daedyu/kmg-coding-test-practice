def star_maker(n: int):
    if n == 3:
        return ['***', '* *', '***']

    small_star = star_maker(n // 3)

    arr = list()

    for i in range(3):
        for line in small_star:
            if i == 1:
                arr.append(line + ' ' * len(line) + line)
            else: arr.append(line * 3)

    return arr


n = int(input())

for i in star_maker(n):
    print(i)