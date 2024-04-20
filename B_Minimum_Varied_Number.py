t = int(input())
for _  in range(t):
    
    num = int(input())
    res = ""
    while num > 0:
        for i in range(9, -1, -1):
            if num - i > 0:
                res += str(i)
                num -= i
            else:
                res += str(num)
                num = 0
                break
    print(res[::-1])