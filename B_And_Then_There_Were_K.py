t = int(input())
for _ in range(t):
    n = int(input())

    shift = n.bit_length() -1
    ans = "1" * shift
    if not ans:
        ans = "0"
    res = int(ans, 2)
    print(res)
    
