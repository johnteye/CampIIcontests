t = int(input())
for _ in range(t):
    
    arr = list(map(str, input().strip()))

    if arr.count("A") > arr.count("B"):
        print("A")

    else:
        print("B")