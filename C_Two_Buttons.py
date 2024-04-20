source, des = map(int, input().split())
count = 0

while des > source:
    if des % 2 == 0:
        temp = des // 2
        count += 1
        des = temp
    else:
        temp = (des+1) // 2
        count += 2
        des = temp


while des < source:
    source -= 1
    count += 1
    

print(count)

