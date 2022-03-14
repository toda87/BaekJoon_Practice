num = int(input())

dp = [[0] * 10 for _ in range(num + 1)]

for i in range(1, 10):
    dp[1][i] = 1

LIMIT = 1000000000

for i in range(2, num + 1):
    for j in range(0, 10):
        # Can only go to 1
        if j==0:
            dp[i][j] = dp[i-1][1]
        # Can only go to 8
        elif j==9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[num]) % LIMIT)
