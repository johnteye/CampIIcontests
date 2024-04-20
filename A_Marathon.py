t = int(input())
for _ in range(t):
    arr = list(map(int , input().split()))
    t = arr[0]
    n = len(arr)
    res = 0

    for i in range(1, n):
        if arr[i] > t:
            res += 1

    print(res)