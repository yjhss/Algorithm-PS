t = int(input())

# DFS
def dfs(v):
  visited[v] = True 
  nv = graph[v]    
  if not visited[nv]:
    dfs(nv)
  
for _ in range(t):
  n = int(input())
  graph = list(map(int, input().split()))
  graph.insert(0, 0)  
  visited = [False] * (n + 1)
  count = 0

  for i in range(1, n + 1):
    if not visited[i]:
      dfs(i)     
      count += 1
  print(count)