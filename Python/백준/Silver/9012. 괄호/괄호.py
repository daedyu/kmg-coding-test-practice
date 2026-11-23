def vps(data: list):
    queue = list()
    for i in data:
        if i == '(':
            queue.append(i)
        else:
            if not queue:
                return False
            queue.pop()
    return True if not queue else False

n = int(input())

for _ in range(n):
    print( 'YES' if vps(list(input())) else 'NO')