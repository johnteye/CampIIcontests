def ans(val):
    res = 0
    while val > 0:
        # print(val)
        if val == 1:
            return res
        elif val % 2 == 0 and val >= 6 and val % 6 == 0:
        
            res += 1
            val = val / 6
        elif val % 2 == 1 and val >= 3 and val % 3 == 0:
            res += 2
            val = val / 3
        elif val < 3:
            return -1
        else:
            return -1
    
    return res

t = int(input())
for _ in range(t):
    val =  int(input())

  
    print(ans(val))
    