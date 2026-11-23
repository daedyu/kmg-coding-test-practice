n = int(input())
rows  = 2 * n
width = 4 * n + 2

for i in range(rows):
    line = [' '] * width

    line[(2*n - 1) - i] = '*'

    if i < n:
        line[3*n - i] = '*'
    else:
        line[n + 1 + i] = '*'

    if i < n:
        line[3*n + 2 + i] = '*'
    else:
        line[3*n + 2 + (2*n - 1 - i)] = '*'

    print(''.join(line))