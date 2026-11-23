from collections import deque

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'R': ri, rj = i, j; arr[i][j] = '.'
        elif arr[i][j] == 'B': bi, bj = i, j; arr[i][j] = '.'
        elif arr[i][j] == 'O': oi, oj = i, j

def slide(ri, rj, bi, bj, di, dj):
    nri, nrj = ri, rj
    while True:
        ni, nj = nri + di, nrj + dj
        if arr[ni][nj] == '#': break
        nri, nrj = ni, nj
        if (nri, nrj) == (oi, oj): break  # 홀에 빠짐

    r_in_hole = (nri, nrj) == (oi, oj)

    nbi, nbj = bi, bj
    while True:
        ni, nj = nbi + di, nbj + dj
        if arr[ni][nj] == '#': break
        nbi, nbj = ni, nj
        if (nbi, nbj) == (oi, oj): break

    b_in_hole = (nbi, nbj) == (oi, oj)

    if b_in_hole:
        return None

    if (nri, nrj) == (nbi, nbj):
        if not r_in_hole:
            if di == 0:
                if dj > 0:
                    if rj > bj: nbi -= di; nbj -= dj
                    else: nri -= di; nrj -= dj
                else:
                    if rj < bj: nbi -= di; nbj -= dj
                    else: nri -= di; nrj -= dj
            else:
                if di > 0:
                    if ri > bi: nbi -= di; nbj -= dj
                    else: nri -= di; nrj -= dj
                else:
                    if ri < bi: nbi -= di; nbj -= dj
                    else: nri -= di; nrj -= dj

    return (nri, nrj, nbi, nbj), r_in_hole

dirs = [(-1,0),(1,0),(0,-1),(0,1)]
visited = set()
queue = deque()
start = (ri, rj, bi, bj)
queue.append((start, 0))
visited.add(start)

while queue:
    (ri, rj, bi, bj), depth = queue.popleft()

    if depth >= 10:
        break

    for di, dj in dirs:
        result = slide(ri, rj, bi, bj, di, dj)
        if result is None:
            continue
        (nri, nrj, nbi, nbj), r_in_hole = result
        if r_in_hole:
            print(depth + 1)
            exit()
        state = (nri, nrj, nbi, nbj)
        if state not in visited:
            visited.add(state)
            queue.append((state, depth + 1))

print(-1)