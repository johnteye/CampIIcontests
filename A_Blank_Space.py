t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    count = 0
    maxi = 0
    for val in arr:
        
        if val == 0:
            count += 1
            maxi = max(maxi, count)

        else:
            count = 0

    print(maxi)