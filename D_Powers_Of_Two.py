n, k = map(int, input().split())
def solve(n):
    arr = []
    res = []
    for i in range(n//2+1):
        num = 1<<i
        if num <= n: arr.append(num)
    print(arr)
    for j in range(len(arr)):
        
        # if len(res) == k:
        #     return res
        print(n)
        while arr[j] <= n:
            n -= arr[j]
            res .append(arr[j])
    return res

print(solve(n))
