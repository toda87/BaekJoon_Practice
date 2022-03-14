iter = int(input())

dp = [0, 1, 2, 4]

max_num = -1

inputs = []

for i in range(iter):
    next_input = int(input())
    inputs.append(next_input)
    if next_input > max_num:
        max_num = next_input

for i in range(4, max_num + 1):
    dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])

for i in range(len(inputs)):
    print(dp[inputs[i]])
