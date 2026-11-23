arr = input().split('.')

def poliomino(n, newstr):
    if n == 4:
        return newstr + 'AAAA'
    elif n == 2:
        return newstr + 'BB'
    elif n > 4:
        return poliomino(n - 4, newstr + 'AAAA')
    elif n > 2:
        return poliomino(n - 2, newstr + 'BB')
    else:
        return -1

for i in range(len(arr)):
    if arr[i] == '':
        continue
    poli = poliomino(len(arr[i]), '')
    if poli != -1:
        arr[i] = poli
    else:
        print(-1)
        exit()

print('.'.join(arr))