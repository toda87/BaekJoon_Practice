from sys import stdin
from collections import deque

input = stdin.readline

n, m = map(int, input().split())

a = [list(input().strip()) for _ in range(n)]
check = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
q = deque()


def init():
    _rx, _ry, _bx, _by = [0] * 4
    for i in range(n):
        for j in range(m):
            if a[i][j] == 'R':
                _rx, _ry = i, j
            elif a[i][j] == 'B':
                _bx, _by = i, j
    q.append((_rx, _ry, _bx, _by, 0))
    check[_rx][_ry][_bx][_by] = True


# Ball moves towards a direction until it finds a hole or it hits a wall
def move(_x, _y, _dx, _dy):
    ctr = 0
    while a[_x + _dx][_y + _dy] != '#' and a[_x][_y] != 'O':
        _x += _dx
        _y += _dy
        ctr += 1
    return _x, _y, ctr


def bfs():
    while q:
        rx, ry, bx, by, d = q.popleft()
        if d > 10:
            break

        # For all directions
        for i in range(4):
            # Calculate the coordinate after movement and the distance it travelled
            nrx, nry, rc = move(rx, ry, dx[i], dy[i])
            nbx, nby, bc = move(bx, by, dx[i], dy[i])

            # If blue ball falls into the hole
            if a[nbx][nby] == 'O':
                continue

            # If red ball falls into the hole
            if a[nrx][nry] == 'O':
                print(d+1)
                return

            # If two balls are at the same location
            if nrx == nbx and nry == nby:
                if rc > bc:
                    nrx, nry = nrx - dx[i], nry - dy[i]
                else:
                    nbx, nby = nbx - dx[i], nby - dy[i]

            # If the coordinate has not been already checked, check it and increase count
            if not check[nrx][nry][nbx][nby]:
                check[nrx][nry][nbx][nby] = True
                q.append((nrx, nry, nbx, nby, d + 1))
    print(-1)


init()
bfs()
