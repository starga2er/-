from collections import deque

N, M = map(int, input().split())

nmap = [ [1]*(M+2) for _ in range(N+2)]
visited = [[[1000001]*2 for _ in range(M+2)] for __ in range(N+2)]

for i in range(N):
    m = input()
    for j in range(M):
        nmap[i+1][j+1] = int(m[j])

queue = deque()

visited[1][1][0] = 1

queue.append((1,1,0))

dx = [1,0,-1,0]
dy = [0,1,0,-1]

while len(queue) != 0:
    y,x,blockbreak = queue.popleft()
    if (y,x) == (N, M):
        print(visited[N][M][blockbreak])
        quit()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (0 <= nx <= M and 0 <= ny <= N):
            continue

        if nmap[ny][nx] == 0 and visited[ny][nx][blockbreak] > visited[y][x][blockbreak] +1:
            queue.append((ny,nx,blockbreak))
            visited[ny][nx][blockbreak] = visited[y][x][blockbreak] +1
        
        if blockbreak == 0 and nmap[ny][nx] == 1 and visited[ny][nx][1] > visited[y][x][0] + 1:
            queue.append((ny,nx, 1))
            visited[ny][nx][1] = visited[y][x][0] + 1


print(-1)
    