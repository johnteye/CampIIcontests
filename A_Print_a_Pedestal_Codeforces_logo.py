import math
t = int(input())

for _ in range(t):
    num = int(input())
    first, second, third = 0, 0, 0

    second = math.ceil(num / 3)
    if second + (second + 1) == num:
        first = second + 1
        second -= 1
    else:
        first = second + 1
    third = num - (first + second)

    print(second, first, third)
