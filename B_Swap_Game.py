# def solve(val):
#     while val > 0:
        
#         if (val - 3) >= 0:
#             val -= 3
#             if val == 0:
#                 return "Alice"
        
#         if  (val - 2) >= 0:
#             val -= 2
#             if val == 0:
#                 return "Bob"
            
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     arr = list(map(int, input().split()))
#     val = sum(arr)
#     if val == 1:
#         print("Alice")
#     else:
#         print(solve(val))

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    if arr[0] > min(arr[1:]):
        print("Alice")
    else:
        print("Bob")