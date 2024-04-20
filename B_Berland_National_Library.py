n = int(input())

current_visitors = 0
max_visitors = 0
visitors = set()

for i in range(n):
    event = list(map(str, input().split()))
    if event[0] == '+':
        visitors.add(event[1])
        current_visitors += 1
    else:
        if event[1] in visitors:
            visitors.remove(event[1])
            current_visitors -= 1
        else:
            max_visitors += 1
    max_visitors = max(max_visitors, current_visitors)

print(max_visitors)
