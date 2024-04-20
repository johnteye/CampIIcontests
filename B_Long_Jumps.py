t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    dp = [0] * (n)

    for i in range(n-1, -1, -1):
        in_index = i + arr[i]
        dp[i] = arr[i]

        if in_index < n:
            dp[i] += dp[in_index]

    print(max(dp))