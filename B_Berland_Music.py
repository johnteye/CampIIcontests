from collections import Counter
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    rating = str(input())
    ans , likes , dislikes = [], [], []
    
    for i in range(n):
        if rating[i] == "0":
            dislikes.append(arr[i])
        else:
            likes.append(arr[i])

    total = sorted(dislikes) + sorted(likes)
    hashmap = {total[i]: i+ 1 for i in range(n)}
    for val in arr:
        ans.append(hashmap[val])
    return ans

t =  int(input())
for _ in range(t):
    print(*solve())