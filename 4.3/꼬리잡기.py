n, m, k = map(int,input().split())

def func(n):
    return [int(n),0]

nlist = [list(map(func,input().split())) for i in range(n)]
visited = [[False]*n for i in range(n)]
head = []
tail = []

dx = [1,0,-1,0]
dy = [0,-1,0,1]

def build_num(y,x, num):
    global nlist, visited, head, tail
    visited[y][x]=True
    nlist[y][x][1]=num

    if nlist[y][x][0] == 1:
        head.append([y,x])
    elif nlist[y][x][0] == 3:
        tail.append([y,x])

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<= nx <n and 0 <= ny < n and not visited[ny][nx] and (nlist[ny][nx][0] == 2 or nlist[ny][nx][0] == 3):
            return build_num(ny,nx, num)

def head_len(y,x,num):
    global nlist, head

    visited = [[False]*n for i in range(n)]

    hy, hx = head[num][0], head[num][1]
    visited[hy][hx] = True
    if (y,x) == (hy,hx):
        return 1
    else:
        nx =0
        ny =0
        for i in range(4):
            nx = hx + dx[i]
            ny = hy + dy[i]

            if 0<= nx <n and 0 <= ny < n and nlist[ny][nx][0] == 2:
                break
        ans = 2
        while True:
            visited[ny][nx] = True
            if (nx,ny) == (x,y):
                return ans
            
            if  nlist[ny][nx][0] == 3:
                print('bug')
                return ans
            
            for i in range(4):
                nnx = nx + dx[i]
                nny = ny + dy[i]
                if 0<= nnx < n and 0 <= nny < n and not visited[nny][nnx] and (nlist[nny][nnx][0] == 2 or nlist[nny][nnx][0] == 3):
                    ny,nx = nny,nnx
                    ans += 1
                    break
            

        
def move():
    global m, head, tail
    for i in range(m):
        for j in range(4):
            nx = tail[i][1] + dx[j]
            ny = tail[i][0] + dy[j]

            if 0<= nx <n and 0 <= ny < n and nlist[ny][nx][0] == 2:
                nlist[tail[i][0]][tail[i][1]] = [4,i]
                # nlist[ny][nx] = [3,i]
                tail[i] = [ny,nx]
                break

        for j in range(4):
            nx = head[i][1] + dx[j]
            ny = head[i][0] + dy[j]

            if 0<= nx <n and 0 <= ny < n and (nlist[ny][nx][0] == 4 or nlist[ny][nx][0] == 3):
                nlist[head[i][0]][head[i][1]] = [2,i]
                nlist[ny][nx] = [1,i]
                head[i] = [ny,nx]
                break
        nlist[tail[i][0]][tail[i][1]] = [3,i]
        
def check(round):
    global n,dx,dy
    pattern = round%(4*n)
    way = pattern//n
    point = pattern % n
    x, y = 0, 0
    if way == 0:
        y = point
    elif way == 1:
        x = point
        y = n-1
    elif way == 2:
        x = n -1
        y = n-1 -point
    elif way == 3:
        x = n-1 -point
        y = 0
    ans = 0
    while 0<= x <n and 0<= y <n:
        
        if nlist[y][x][0] != 0 and nlist[y][x][0] != 4:
            # print(x,y)
            temp =  head_len(y,x, nlist[y][x][1])
            num = nlist[y][x][1]
            nlist[head[num][0]][head[num][1]][0] = 3 
            nlist[tail[num][0]][tail[num][1]][0] = 1
            t = head[num][0], head[num][1]
            head[num] = tail[num]
            tail[num] = t
            return temp

        x = x + dx[way]
        y = y + dy[way]
    return ans

num = 0
for i in range(n):
    for j in range(n):
        if nlist[i][j][0] == 1:
            build_num(i,j,num)
            num += 1
wpoint = 0
for round in range(k):
    move()
    # for i in range(n):
    #     print(nlist[i])
    wpoint += check(round) ** 2
    # print(wpoint)
print(wpoint)
