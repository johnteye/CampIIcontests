word = list(map(str, input().strip()))
def machine(word):
    n = len(word)
    dp = [0] * (n+1)
    dp[0] = 1

    for i in range(1, n+1):
        if word[i-1] == "m" or word[i-1] == "w":
            return 0
        elif word[i-1] == word[i-2] and (word[i-1] == "u" or word[i-1] == "n"):
            dp[i] = dp[i-1] + dp[i-2]

        else:
            dp[i] = dp[i-1]


    return (dp[-1] % ((10**9) + 7) )

print(machine(word))

