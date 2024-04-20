# import sys
# import threading

# sys.setrecursionlimit(1 << 30)
# threading.stack_size(1 << 27)

# def main():
#     def solve():
#         n = int(input())
#         memo = {}
#         word = str(input())
#         cost = list(map(int, input().split()))

#         check = "hard"
#         memo = {}

#         def dp(i, j):
#             if (i,j) in memo:
#                 return memo[(i, j)]
           
#             if j >= 4:
#                 return float("inf")
#             if i >= n :
#                 return 0
            
#             if word[i] == check[j]:
#                 memo[(i, j)]=  min(dp(i+1, j) + cost[i], dp(i+1, j + 1))
#             else:
#                 memo[(i, j)] =  dp(i+1, j)

#             return memo[(i, j)]

#         return dp(0, 0) if dp(0, 0) != float("inf") else 0
#     print(solve())
# main_thread = threading.Thread(target=main)
# main_thread.start()
# main_thread.join()

    

n=int(input())
s=input() 
Dict = {"h": 0, "a": 0, "r": 0, "d": 0}
cost= list(map(int,input().split()))
for i in range(n):
    if s[i]=='h':
        Dict['h']+=cost[i]
    if s[i]=='a':
        Dict['a']=min(Dict['a']+cost[i],Dict['h'])
    if s[i]=='r':
        Dict['r']=min(Dict['r']+cost[i],Dict['a'])
    if s[i]=='d':
        Dict['d']=min(Dict['d']+cost[i],Dict['r'])
print(Dict['d'])