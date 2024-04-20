from collections import Counter
def solve():
    n = int(input())
    arr = list(map(str, input().strip()))

    if n % 2 == 1:
        return n
    arr1 = arr[:n//2]
    check = arr[n//2:]
    
    if set(arr1) == set(check):
        return n
    if len(set(arr)) < 3:
        return 1
    for i in range(n//2 + 1):
        if arr1[i] != check[i]:
            return i+ 1 if (i+1) % 2 == 0 else n // 2
        
t = int(input())
for _ in range(t):
    print(solve())


        