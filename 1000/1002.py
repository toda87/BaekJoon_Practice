import math

test_case = int(input())

def get_intersection(x0, x1, y0, y1, r0, r1):
    d=math.sqrt((x1-x0)**2 + (y1-y0)**2)

    # non intersecting
    if d > r0 + r1 :
        return 0
    # One circle within other
    if d < abs(r0-r1):
        return 0
    # coincident circles
    if d == 0 and r0 == r1:
        return -1
    else:
        a=(r0**2-r1**2+d**2)/(2*d)
        h=math.sqrt(r0**2-a**2)
        x2=x0+a*(x1-x0)/d
        y2=y0+a*(y1-y0)/d
        x3=x2+h*(y1-y0)/d
        y3=y2-h*(x1-x0)/d

        x4=x2-h*(y1-y0)/d
        y4=y2+h*(x1-x0)/d

    if x3 == x4 and y3 == y4:
        return 1
    else:
        return 2

for i in range(test_case):
    curr_test = input().split()
    x1 = int(curr_test[0])
    y1 = int(curr_test[1])
    r1 = int(curr_test[2])

    x2 = int(curr_test[3])
    y2 = int(curr_test[4])
    r2 = int(curr_test[5])

    # if two guys are at the same location
    print(get_intersection(x1, x2, y1, y2, r1, r2))
    #

