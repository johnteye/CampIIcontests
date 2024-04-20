from collections import defaultdict

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    letters = list(map(str, input().strip()))
    hashmap = defaultdict(set)
    
    
    for i in range(n):
        hashmap[arr[i]].add(letters[i])

    for val in hashmap:
        if len(hashmap[val]) > 1:
            print("NO")
            break

    else:
        print("YES")