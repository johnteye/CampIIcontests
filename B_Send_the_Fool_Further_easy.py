from collections import defaultdict

n = int(input())
graph = defaultdict(list)

for i in range(n-1):
    u, v , c = map(int, input().split())
    graph[u].append((v, c))
    graph[v].append((u, c))
    

visited = set()
ans = 0

def dfs(node, cost):
    global ans
    visited.add(node)

    ans = max(ans, cost)
    
    for child, c in graph[node]:
        if child not in visited:
            dfs(child, cost + c)
  
dfs(0, 0)  
print(ans)