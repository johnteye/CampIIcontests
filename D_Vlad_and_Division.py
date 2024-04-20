t = int(input())

for _ in range(t):
    n= int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    group = 0
    
    for i in range(n):
        for j in range(i+1, n):
            if ~(arr[i] | arr[j]) != 0:
                group += 1

    print(group)