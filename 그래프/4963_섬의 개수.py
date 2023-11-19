import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1, 1, -1, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph[y][x] = 0
    while queue:
       a, b = queue.pop()
       for i in range(8):
           ny = b + dy[i]
           nx = a + dx[i]
           if 0 <= nx < m and 0 <= ny <n and graph[ny][nx] == 1:
               queue.append((nx, ny))
               graph[ny][nx] = 0

count = []
while True:
    cnt = 0
    m, n = map(int, input().split())
    if n == 0 and m == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(j, i)
                cnt += 1
    count.append(cnt)

for i in count:
    print(i)