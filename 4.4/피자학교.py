from collections import defaultdict
from collections import deque

n, k = map(int,input().split())

nlist = list(map(int,input().split()))
ans = 0 
while True:
    nmap = [[0]*100 for i in range(100)]


    m = min(nlist)
    ma = max(nlist)
    if ma - m <= k:
        print(ans)
        break

    for i in range(n):
        if nlist[i] == m:
            nlist[i] += 1
        nmap[99][i] = nlist[i]


    rollx = 1
    rolly = 1
    x, y = 0,99
    bottom = n
    while True:
        bottom -= rollx
        if bottom < rolly:
            break
        x += rollx
        for i in range(rollx):
            for j in range(rolly):
                nx, ny = -i-1, -j
                # print(nx,ny , nmap[y+ny][x+nx])
                nmap[y+nx][x-ny] = nmap[y+ny][x+nx]
                nmap[y+ny][x+nx] = 0
        
        if rolly == rollx :
            rolly +=1
        else :
            rollx +=1

    def dfs():
        global nmap
        visited = [[False]*100 for i in range(100)]
        q = deque()
        memory = defaultdict(lambda: 0)
        q.append((x,y))
        visited[y][x] = True

        dx = [1,0,-1,0]
        dy = [0,1,0,-1]

        while len(q) != 0:
            nx, ny = q.popleft()
            for i in range(4):
                new_x, new_y = nx + dx[i], ny + dy[i]
                if 0 <= new_x < 100 and 0 <= new_y < 100 :
                    # 
                    # print(new_x,new_y)
                    if nmap[new_y][new_x] != 0 :
                        if nmap[new_y][new_x] < nmap[ny][nx]:
                            weight = (nmap[ny][nx] - nmap[new_y][new_x]) // 5
                            memory[(new_x,new_y)] += weight
                            memory[(nx,ny)] -= weight
                        else :
                            weight = (nmap[new_y][new_x] - nmap[ny][nx]) // 5
                            memory[(new_x,new_y)] -= weight
                            memory[(nx,ny)] += weight
                        if not visited[new_y][new_x] :
                            q.append((new_x, new_y))
                            visited[new_y][new_x] = True

        for kx, ky in memory.keys():
            nmap[ky][kx] += memory[(kx,ky)]//2

    dfs()

    def spread():
        global nmap, y , x
        nx = x
        newlist = []
        while nx < 100 :
            if nmap[y][nx] == 0:
                break
            for i in reversed(range(100)):
                if nmap[i][nx] != 0:
                    newlist.append(nmap[i][nx])
                else :
                    nx += 1
                    break
        return newlist
            
    nlist = spread()
    # print(nlist)
    nmap = [[0]*100 for i in range(100)]
    for i in range(n):
        nmap[99][i] = nlist[i]

    x, y = 0,99
    bottom = n
    for t in range(2):
        bottom = bottom//2
        x += bottom
        for i in range(bottom):
            for j in range(t+1):
                nx, ny = -i-1, -j
                # print(nx,ny , nmap[y+ny][x+nx])
                nmap[y+ny-1][x-nx-1] = nmap[y-ny][x+nx]
                nmap[y-ny][x+nx] = 0
        y = 98
        
    dfs()
    nlist = spread()
    
    ans += 1


#밀가루넣기
#도우말기
#누르기
#도우 두번 반으로 접기
#누르기