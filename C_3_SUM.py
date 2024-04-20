t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    remainder = []

    for i in range(n):
        if remainder.count(arr[i]%10) < 3:
            remainder.append(arr[i]%10)
    # print(remainder)
    
    def solve(arr):
        n = len(arr)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if str(arr[i] + arr[j] + arr[k])[-1] == "3": 
                        return "YES"
                        
        return "NO"
        
    print(solve(remainder))