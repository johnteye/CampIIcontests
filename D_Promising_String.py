t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(str, input().strip()))
    res = 0 
    for i in range(n):
        pos, neg = 0, 0
        for j in range(i, n):
            if arr[j] == "+":
                pos += 1
            else:
                neg += 1

            if pos == neg or (neg > pos and (neg-pos)% 3 == 0):
                res += 1

    print(res)
