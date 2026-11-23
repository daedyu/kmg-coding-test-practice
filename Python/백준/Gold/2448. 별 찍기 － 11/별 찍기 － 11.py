def star_maker(n: int):
    if n == 3:
        return ['  *  ', ' * * ', '*****']

    small_star = star_maker(n // 2)

    arr = list()

    for i in range(2):
        for line in small_star:
            if i == 1:
                arr.append(line + ' ' + line)
            else:
                arr.append(f'{line:^{n * 2 - 1}}')

    return arr


n = int(input())

for i in star_maker(n):
    print(f'{i:^{n * 2}}')