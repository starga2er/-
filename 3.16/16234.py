from collections import deque

N, L, R = map(int,input().split())

visited_map = [[0]*N for i in range(N)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
ispass = True

nlist = []
for i in range(N):
    nlist.append(list(map(int,input().split())))

def dfs(y,x): # return same list
    global visited_map, nlist, ispass
    visited_map[y][x] = 1
    answer = [(y,x)]
    queue = deque()
    queue.append((y,x))
    n = nlist[y][x]
    while len(queue) != 0:
        y,x = queue.pop()
        for k in range(4):
            ny = y+dy[k]
            nx = x+dx[k]
            if 0 <=nx <N and 0 <=ny <N and visited_map[ny][nx] == 0 and L <= abs(nlist[ny][nx] - nlist[y][x]) <= R:
                ispass= True
                answer.append((ny,nx))
                queue.append((ny,nx))
                n += nlist[ny][nx]
                visited_map[ny][nx] = 1
    for y,x in answer:
        nlist[y][x] = n//len(answer)

ans = -1
while ispass:
    ispass = False
    for i in range(N):
        for j in range(N):
            if visited_map[i][j] == 0:
                dfs(i,j)
    ans +=1
    visited_map = [[0]*N for i in range(N)]
print(ans)