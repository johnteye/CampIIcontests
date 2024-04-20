t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    check = sorted(arr)
    
    if k > 1:
        print("YES")
    
    elif k <= 1 and arr == check:
        print("YES")

    else:
        print("NO")