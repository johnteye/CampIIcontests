n = int(input())

dp = [float("inf") for _ in range(8)]
dp[0] = 0

for i in range(n):
    price, vitamin = input().split()
    price = int(price)

    sum_ = 0

    if "A" in vitamin: sum_ |= 1
    if "B" in vitamin: sum_ |= 2
    if "C" in vitamin: sum_ |= 4

    for i in range(8):
        dp[i|sum_] = min(dp[i|sum_], dp[i]+price)

print(dp[-1] if dp[-1] != float("inf") else -1)
    
    

    
    
    





