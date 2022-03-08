board_size = int(input()) + 2
apple_count = int(input())

apple_loc = []

for i in range(apple_count):
    apple_loc.append(list(map(int, list(input().split()))))

move_count = int(input())

movements = []

for i in range(move_count):
    tmp = input().split()
    tmp[0] = int(tmp[0])
    movements.append(tmp)

# Right, Left, Down, Up
dx, dy = (1, 0, -1, 0), (0, 1, 0, -1)


def solve():
    head = [1, 1]
    snake = []
    limit, direc = 0, 0

    snake.append(head)

    while limit < 10000:

        if len(movements) > 0:
            if limit == movements[0][0]:
                if movements[0][1] == 'D':
                    direc = (direc + 1) % 4
                else:
                    direc = (direc - 1) % 4

                del movements[0]

        # move
        head = [head[0] + dy[direc], head[1] + dx[direc]]
        # print(head, len(snake), limit + 1)

        if head in snake:
            #print("hit snake")
            break

        # If the snake hits the wall
        if head[0] <= 0 or head[1] <= 0 or head[0] >= board_size-1 or head[1] >= board_size-1:
            #print("hit wall")
            break

        # Insert snake head
        snake.insert(0, head)

        if len(apple_loc) > 0 and head in apple_loc:
            apple_index = apple_loc.index(head)
            del apple_loc[apple_index]
        else:
            del snake[-1]

        limit += 1

    print(limit + 1)

solve()