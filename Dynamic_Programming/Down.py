import sys
sys.setrecursionlimit(200000)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

M, N = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]


def dfs(x, y):
    if dp[x][y] != -1:
        return dp[x][y]

    # Bottom-Right = Base Case
    if x == M - 1 and y == N - 1:
        return 1

    dp[x][y] = 0

    for i in range(len(dx)):
        curr_dx, curr_dy = x + dx[i], y + dy[i]

        if 0 <= curr_dx <= M - 1 and 0 <= curr_dy <= N - 1:
            if nums[x][y] > nums[curr_dx][curr_dy]:
                dp[x][y] += dfs(curr_dx, curr_dy)

    return dp[x][y]


print(dfs(0, 0))
