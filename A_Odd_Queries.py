t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    sum_ = sum(arr)
    prefix = [0]
    for val in arr:
        prefix.append(prefix[-1] + val)

    for i in range(k):
        l, r, k = map(int, input().split())
        res = sum_

        remove = prefix[r] - prefix[l-1]
        res -= remove

        add = (l - r+1) * k

        res += add

        if res %2 == 0:
            print("NO")
        else:
            print("YES")
        