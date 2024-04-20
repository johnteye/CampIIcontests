t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    ass = list(map(int, input().split()))
    ass.sort(reverse=True)
    gift = list(map(int, input().split()))
    cost , j = 0, 0
    # print(ass)
    for i in range(n):
        if ass[i] > j:
            cost += gift[j]
            j += 1
        else:
            cost += gift[ass[i]-1]
        
    print(cost)