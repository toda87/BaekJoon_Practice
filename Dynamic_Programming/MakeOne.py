num = int(input())

# Solve bottom-up. Let index indicate the number
min_op = [0] * (num+1)

for i in range(2, num + 1):
    # Option 1: Add 1
    min_op[i] = min_op[i - 1] + 1

    # Option 2: Divide by 2
    if i % 2 == 0:
        min_op[i] = min(min_op[i], min_op[int(i / 2)] + 1)

    # Option 3: Divide by 3
    if i % 3 == 0:
        min_op[i] = min(min_op[i], min_op[int(i / 3)] + 1)

print(min_op[num])