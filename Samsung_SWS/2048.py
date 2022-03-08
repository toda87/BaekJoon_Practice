import copy, math

# n = board size
n = int(input())
max_iter = 5

board = [list(map(int, list(input().split()))) for _ in range(n)]

# left, right, down, up
dx, dy = (-1, 1, 0, 0), (0, 0, 1, -1)

# Build Record Map
# Iterative increase size based on the depth (iteration) of the algorithm
record = []
for i in range(max_iter):
    tmp = []
    iter_range = int(math.pow(len(dx), i + 1))
    for j in range(iter_range):
        tmp_2 = []
        for k in range(len(dx)):
            tmp_2.append(list(list([0] * n) for _ in range(n)))
        tmp.append(tmp_2)
    record.append(tmp)


def get_max(list):
    max = -1
    for i in range(n):
        for j in range(n):
            if list[i][j] > max:
                max = list[i][j]

    return max


def move(curr_board, i, j, curr_dx, curr_dy, tracker):
    curr_val = curr_board[i][j]

    # If value is 0, skip
    if curr_val == 0:
        return

    tmp_i, tmp_j = i + curr_dy, j + curr_dx

    while curr_board[tmp_i][tmp_j] == 0:
        if curr_dy == 0:
            if curr_dx < 0 and tmp_j <= 0:  # Left
                break
            elif curr_dx > 0 and tmp_j >= n - 1:  # Right
                break

        if curr_dx == 0:
            if curr_dy < 0 and tmp_i <= 0:
                break
            elif curr_dy > 0 and tmp_i >= n - 1:
                break

        tmp_i += curr_dy
        tmp_j += curr_dx

    # Delete value from the board
    curr_board[i][j] = 0

    if curr_val == curr_board[tmp_i][tmp_j] and not tracker[tmp_i][tmp_j]:
        curr_board[tmp_i][tmp_j] *= 2
        tracker[tmp_i][tmp_j] = True
    # If 0, change value to the current value
    elif curr_board[tmp_i][tmp_j] == 0:
        curr_board[tmp_i][tmp_j] = curr_val
    else:
        curr_board[tmp_i - curr_dy][tmp_j - curr_dx] = curr_val


def get_new_board(curr_board, curr_dy, curr_dx):
    # Column-wise Traversal
    tracker = [[0] * n for _ in range(n)]

    if curr_dy == 0:  # LEFT and RIGHT
        start, end = (1, n) if curr_dx == -1 else (n - 2, -1)

        for j in range(start, end, -curr_dx):
            for i in range(n):
                move(curr_board, i, j, curr_dx, curr_dy, tracker)

    # Row-wise Traversal
    else:  # Up and Down
        start, end = (1, n) if curr_dy == -1 else (n - 2, -1)

        for i in range(start, end, -curr_dy):
            for j in range(n):
                move(curr_board, i, j, curr_dx, curr_dy, tracker)

    return curr_board


def solve():

    # When the board size is 1 X 1
    if n == 1:
        return board[0][0]

    overall_max = -1
    for i in range(5):
        # 4 Possible directions
        for j in range(4):
            curr_dx = dx[j]
            curr_dy = dy[j]
            if i == 0:
                curr_board = copy.deepcopy(board)
                record[i][j] = get_new_board(curr_board, curr_dy, curr_dx)
            else:
                for k in range(len(record[i - 1])):
                    idx = len(record[i - 1]) * j + k
                    curr_board = copy.deepcopy(record[i - 1][k])
                    record[i][idx] = get_new_board(curr_board, curr_dy, curr_dx)

                    if i == 4:
                        curr_max = get_max(record[i][idx])
                        if get_max(record[i][idx]) > overall_max:
                            overall_max = curr_max

    return overall_max


print(solve())
