import sys
input = lambda: sys.stdin.readline().rstrip()

arr = 0

for _ in range(int(input())):
    data = input().split()

    if data[0] == 'add':
        arr |= (1 << int(data[1]))
    elif data[0] == 'remove':
        arr &= ~(1 << int(data[1]))
    elif data[0] == 'check':
        print(1 if arr & (1 << int(data[1])) else 0)
    elif data[0] == 'toggle':
        arr ^= (1 << int(data[1]))
    elif data[0] == 'all':
        arr = (1 << 21) - 1
    else:
        arr = 0