from collections import deque

N, M = map(int, input().split())

nmap = [ [0]*(M+2) for _ in range(N+2)]

for i in range(N):
    m = input()
    for j in range(M):
        nmap[i+1][j+1] = int(m[j])

queue = deque()
nmap[1][1] == 0
queue.append((1,1,1))

dx = [1,0,-1,0]
dy = [0,1,0,-1]

while len(queue) != 0:
    y,x,way = queue.popleft()
    if (y,x) == (N, M):
        print(way)
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nmap[ny][nx] == 1:
            queue.append((ny,nx,way+1))
            nmap[ny][nx] = 0
    


