t = int(input())

for _ in range(t):
    arr = input().split("R")
    n = len(arr)
    
    print(max(len(val) for val in arr) + 1)