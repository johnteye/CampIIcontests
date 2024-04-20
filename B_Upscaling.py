# t = int(input())
# for _ in range(t):
#     n = int(input())
#     for i in range(2 * n):
#         for j in range(n):
#             if (i// 2 + j) % 2 == 0:
#                 print("##", end = "")
#             else:
#                 print("..", end = "")
#         print()
    
arr = list(map(int, input().split()))
n = len(arr)
maxx = [0] * (max(arr) + 1)
for val in arr:
    maxx[val] += 1

print(val)

#bubble sort
# for i in range(n):
#     for j in range(i, n):
#         if arr[i] > arr[j]: 
#             arr[i], arr[j] = arr[j], arr[i]

# print(arr)


# Kandane's algorithm

# maxi, mini = 0 , 0
# ans = 0
# for num in arr:
#     maxi = max(maxi+num, 0)
#     mini = min(mini + num, 0)
#     ans = max(mini, maxi , ans)

# print(ans)

# for i in range(n):
#     total = max(arr[i], total + arr[i])
#     ans = max(ans, total)

# print(ans)
# ans = 0
# for i in range(n):
#     total = 0
#     for j in range(i,n):
#         total += arr[j]
#         ans = max(ans, total)

