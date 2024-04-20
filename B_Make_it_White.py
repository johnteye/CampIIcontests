t = int(input())
for _ in range(t):
    n = int(input())
    arr = input().strip()


    for i in range(n):
        if arr[i] == "B":
            left = i
            break

    for j in range(n-1, -1, -1):

        if arr[j] == "B":
            right = j
            break


    print(right-left+1)