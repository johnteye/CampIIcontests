n = int(input())
arr = list(map(int, input().split()))
c, bi,b = True, False , False

c_c, bi_c, b_c = 0, 0, 0

for val in arr:
    if c:
        c_c += val
        c = False
        bi = True
        
    elif bi:
        bi_c += val
        bi = False
        b = True
        
    else:
        b_c += val
        b = False
        c = True
        
        
maxx = max(c_c, bi_c, b_c)
if c_c == maxx:
    print("chest")
elif bi_c == maxx:
    print("biceps")
    
else:
    print("back")