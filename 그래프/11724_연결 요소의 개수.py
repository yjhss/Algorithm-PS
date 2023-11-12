import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000) #재귀 최대깊이

n, m = map(int, input().split())
graph = [[i] for i in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False]*(n+1)  
cnt = 0 

# dfs(탐색할 그래프, 시작 노드, 방문여부 리스트)
def dfs(graph, v, visited):
    visited[v] = True  # 시작 노드 방문
    for i in graph[v]:
        if not visited[i]:  # 방문하지 않은 노드라면
            dfs(graph, i, visited)  # dfs 재귀호출


for i in range(1, n+1):
    if not visited[i]:  # 방문하지 않은 노드라면
        cnt += 1  #cnt 1 증가
        dfs(graph, i, visited)  # dfs 탐색
print(cnt)