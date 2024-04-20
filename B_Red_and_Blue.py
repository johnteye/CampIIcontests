t = int(input())
 
def prefix(arr):
    res = []
    pre_sum = 0
    for val in arr:
        pre_sum += val
        res.append(pre_sum)
    return max(max(res), 0)
 
 
for _ in range(t):
    a = int(input())
    arr_a = list(map(int, input().split()))
    b = int(input())
    arr_b = list(map(int, input().split()))
 
    pref_a = prefix(arr_a)
    pref_b = prefix(arr_b)
 
    ans = pref_a + pref_b
 
    if ans > 0:
        print(ans)
    else:
        print(0)