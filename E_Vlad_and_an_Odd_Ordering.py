t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    for i in range(1, n):
        find = 0
        for j in range(i, n):
            j += i + 2
            find += 1

            if find == k:
                print(j)
                break

