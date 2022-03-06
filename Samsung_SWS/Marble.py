n, m = map(int, input().split())

a = [list(input().strip()) for _ in range(n)]
check = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
q = []

def init():
    _rx, _ry, _bx, _by = [0] * 4
    for i in range(n):
        for j in range(m):
            if a[i][j] == 'R':
                _rx, _ry = i, j
            elif a[i][j] == 'B':
                _bx, _by = i, j
    q.append((_rx, _ry, _bx, _by, 1))
    check[_rx][_ry][_bx][_by] = True


# Ball moves towards a direction until it finds a hole or it hits a wall
def move(x, y, dx, dy):
    ctr = 0
    while a[x + dx][y + dy] != '#' and a[x][y] != 'O':
        x += dx
        y += dy
        ctr += 1
    return x, y, ctr


def solve():
    init()  # 시작 조건
    while q:  # BFS : queue 기준
        rx, ry, bx, by, depth = q.pop(0)
        if depth > 10:  # 실패 조건
            break
        for i in range(4):  # 4방향 이동 시도
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])  # Red
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i])  # Blue
            if a[nbx][nby] != 'O':  # 실패 조건이 아니면
                if a[nrx][nry] == 'O':  # 성공 조건
                    print(depth)
                    return
                if nrx == nbx and nry == nby:  # 겹쳤을 때
                    if rcnt > bcnt:  # 이동거리가 많은 것을
                        nrx -= dx[i]  # 한 칸 뒤로
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                # breadth 탐색 후, 탐사 여부 체크
                if not check[nrx][nry][nbx][nby]:
                    check[nrx][nry][nbx][nby] = True
                    # 다음 depth의 breadth 탐색 위한 queue
                    q.append((nrx, nry, nbx, nby, depth+1))
    print(-1)  # 실패 시

solve()