N, M, V = map(int,input().split())

edges = [[0]*(N+1) for _ in range(N+1)]
visited = [0]*(N+1)

for i in range(M):
    x, y = map(int,input().split())
    edges[x][y] = 1
    edges[y][x] = 1

ans = []

def DFS(n):
    global N, ans
    ans.append(n)
    visited[n] = 1
    for i in range(N+1):
        if edges[n][i] == 1 and visited[i] == 0:
            DFS(i)

def BFS(n):
    global N, ans, visited
    if n == []:
        return

    ans = ans + n
    checked = []
    for i in n:
        visited[i] = 1
        for j in range(N+1):
            if edges[i][j] == 1 and visited[j] == 0:
                visited[j] = 1
                checked.append(j)
    
    BFS(checked)

DFS(V)
print(*ans)
visited = [0]*(N+1)
ans = []

visited[V] = 1
BFS([V])
print(*ans)