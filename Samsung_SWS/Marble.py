from sys import stdin
from collections import deque

input = stdin.readline

n, m = map(int, input().split())

a = [list(input().strip()) for _ in range(n)]
print(a)
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


def move(_x, _y, _dx, _dy, _c):
    while a[_x + dx][_y + _dy] != '#' and a[_x][_y] != 0:
        _x += dx
        _y += dy
        _c += 1
    return _x, _y, _c
