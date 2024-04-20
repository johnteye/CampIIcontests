t = int(input())

for _ in range(t):
    arr = input().strip()
    val = input()
    n = len(arr)

    for index, char in enumerate(arr):
        if char == val:
            before = index
            after = n - (index + 1)

            if before % 2 == 0 and after % 2 ==0:
                print("YES")
                break




    else:
        print("NO")